import pymongo


class DataAccessLayer:
    def __init__(self):
        self.mongo = MongoDBDataAccessLayer()

    # 按照nid查找
    def find(self, nid: str):
        return self.mongo.find("nya", "profile", {"nid": nid})

    # 按照条件筛选
    def filter(self, data: dict):
        return self.mongo.find("nya", "profile", data)

    # 检测存在
    def exist(self, nid: str):
        if len(self.find(nid)) == 0:
            return False
        else:
            return True

    # 注册
    def new(self, profile: dict):
        self.mongo.new("nya", "profile", profile)
        return True


# MongoDB数据库访问层抽象类
class MongoDBDataAccessLayer:
    def __init__(self):
        # self.mongo_client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
        self.mongo_client = pymongo.MongoClient("mongodb://admin:admin@nya-archive-mongodb:27017/")

    # 增
    def new(self, db_name: str, collect_name: str, data: dict):
        db = self.mongo_client[db_name]
        collect = db[collect_name]
        collect.insert_one(data)

    # 查
    def find(self, db_name: str, collect_name: str, value: dict):
        db = self.mongo_client[db_name]
        collect = db[collect_name]
        result = []
        for item in collect.find(value):
            item.pop('_id')
            result.append(item)
        return result
