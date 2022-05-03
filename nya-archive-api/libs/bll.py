from libs.dal import DataAccessLayer
import uuid
import random
# from pydantic import BaseModel


# class CodeRespond(BaseModel):
#     status_code: int = 0 or 1
#
#
# class DataRespond(BaseModel):
#     status_code: int = 0
#     data: dict or list or str
def empty_random():
    choose = ["[数据编辑]", "[数据删除]", "[数据丢失]", "[未知]", "[访问权限不足]", "▇▇▇▇▇▇", "是秘密哒喵~", "诶嘿"]
    return random.choice(choose)


class BusinessLogicLayer:
    def __init__(self):
        self.dal = DataAccessLayer()

    def check(self, nid: str):
        if self.dal.exist(nid):
            data = self.dal.find(nid)[0]
            for item in data:
                if data[item] == "":
                    data[item] = empty_random()
                else:
                    pass
            return {"status_code": 0, "data": data}
        else:
            return False
            # return CodeRespond(status_code=1).dict()

    def search(self, data):
        tmp = {}
        for item in data:
            if data[item] == "":
                pass
            else:
                tmp[item] = data[item]
        if tmp == {}:
            return False
        else:
            return {"status_code": 0, "data": self.dal.filter(tmp)}

    def new(self, data):
        while True:
            data["nid"] = str(uuid.uuid4())
            if not self.dal.exist(data["nid"]):
                break
            else:
                pass
        data.pop("code")
        if self.dal.new(data):
            return {"status_code": 0, "data": data["nid"]}
        else:
            return False
            # return CodeRespond(status_code=1).dict()
