from SAF.misc.couch_wrapper import CouchWrapper

couchdb_info = {"url": "http://15.32.151.151:5984/", "user":"adminusr", "password":"admin"}
db = CouchWrapper(couchdb_info["url"], "test_package_storage" , (couchdb_info["user"], couchdb_info["password"]))
view = db.setDatabase("test_package_storage").all()
for item in view:
    if item["id"].startswith("_"):
        continue
    #print(item["id"])
    db.deleteRecord(item["id"], dataBase="test_package_storage", purge=True)