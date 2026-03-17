import logging
from time import sleep
from datetime import datetime
from pycouchdb.exceptions import Error, Conflict
from SAF.misc.couch_wrapper import CouchWrapper

class DBUtils(object):
    def __init__(self, couchdb_info):
        self.db_info = couchdb_info
        if self.db_info["url"][-1] == "/":
            self.db_info["url"] = self.db_info["url"][:-1]
        self.package_db_name = "test_package_storage"
        try:
            self.db = CouchWrapper(couchdb_info["url"], self.package_db_name , (couchdb_info["user"], couchdb_info["password"]))
        except Error:
            sleep(3)
            self.db = CouchWrapper(couchdb_info["url"], self.package_db_name , (couchdb_info["user"], couchdb_info["password"]))
    
    def upload_build_to_database(self, rec, attachment_path):
        try:
            if not rec.get("date", False):
                rec["date"] = datetime.now().strftime("%Y-%m-%d")
            doc_id = self.db.saveRecord(rec)["_id"]
            file_name = attachment_path.split("/")[-1]
            self.db.addAttachment(doc_id,attachment_path, file_name.replace(" ", "_"))
            base_url = self.db_info['url'].replace('http://', f'http://{self.db_info["user"]}:{self.db_info["password"]}@')
            return base_url + "/" + self.package_db_name + "/" + doc_id + "/" + file_name.replace(" ", "_")
        except Conflict:
            logging.info("Assuming another process has already uploaded the build")
            #Wait 10 seconds before moving forward just in case
            sleep(10)
            return None

    def check_build_in_database(self, key_match, view_group, view_name, nexus=False):
        view_list = self.db.getAllViewResults(view_group, view_name)
        for item in view_list:
            if not nexus:
                key = item["key"]
            else:
                key = [item["value"]["project"], item["value"].get("artifact_name", None), item["value"].get("app_version", None), item["value"]["os"]]
            if key == key_match:
                if not self.db.fetchRecord(item["value"]["_id"], raise_e=False):
                    continue
                if item["value"].get("_attachments", None) is None:
                    print("No attachment is actually in the document!")
                    self.db.deleteRecord(item["value"]["_id"], dataBase=self.package_db_name, purge=True, raise_e=False)
                    return False
                else:
                    base_url = self.db_info['url'].replace('http://', f'http://{self.db_info["user"]}:{self.db_info["password"]}@')
                    return base_url + "/" + self.package_db_name + "/" + item["value"]["_id"] + "/" + list(item["value"]["_attachments"].keys())[0], item["value"].get("app_info", None)
        return False