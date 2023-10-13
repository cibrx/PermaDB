from cache import CacheDB
from main import PermaDB

db = PermaDB()

print(db.set("test2","tests2"))
print(db.set("test1","tests1"))
print(db.update("test2","asdsaddddd"))
print(db.get("test2"))
print(db.has("test2"))
print(db.fetch("test2"))
print(db.typeof("test2"))
print(db.fileSize())
print(db.vacuum())
print(db.all())
print(db.keys())
print(db.values())
print(db.size())
