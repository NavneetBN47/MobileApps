import datetime as DT
from SAF.misc.couch_wrapper import CouchWrapper

couchdb_info = {"url": "http://15.32.151.151:5984/", "user":"adminusr", "password":"admin"}
db = CouchWrapper(couchdb_info["url"], "test_package_storage" , (couchdb_info["user"], couchdb_info["password"]))

today = DT.date.today()
week_ago = (today - DT.timedelta(days=7)).strftime("%Y-%m-%d")
mango = {"selector": {"date": {"$lt": week_ago}}}
database = db.setDatabase("test_package_storage")
while True:
    view = db.find(mango)["docs"]
    purge_list = []
    for item in view:
        if item["_id"].startswith("_"):
            continue
        print("deleting: " + item["_id"])
        db.deleteRecord(item["id"], purge=True)
        purge_list.append(item)
    if not purge_list:
        break
    
db.totalCleanUp()