import requests
import json
import secrets
import csv
from pydantic import *


ss = requests.session()
root = "http://localhost:9888"
manage_code = "77807aa2f1fcf812544660ea5923fbd33076b9154cb67fef3b7ed7289ff85b82"


def send(data):
    resp = ss.post(root + "/add/", json.dumps(data))
    return json.loads(resp.text)


def random_pack():
    return {
        "name": secrets.token_hex()[:12],
        "color": secrets.token_hex()[:12],
        "features": [],
        "like": [],
        "dislike": [],
        "birth": secrets.token_hex()[:12],
        "sex": True,
        "castrated": True,
        "rip": False,
        "relation": secrets.token_hex()[:12],
        "code": manage_code
    }


def search():
    name = "4af46dcfac8d8fe4c4cd28b8ab0663bc18ffa08ef97d3ad76e0fa9f9e50fe747"
    resp = ss.post(root + "/search/", json.dumps({"name": name}))
    print(resp.text)


def load():
    data = []
    with open("./a.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            tmp = []
            for e in row:
                tmp.append(e)
            data.append(tmp)
        data = data[1:]
    return data


# def format_sex(data):
#     if data == "公":
#         return data
#     elif data == "母":
#         return
#     else:
#         return False


def format_cast(data):
    if data == "公":
        return True
    else:
        return False


def format_as_list(data):
    try:
        tmp = data.split("，")
        return tmp
    except:
        return [data]


def make_pack(data):
    data_pack_list = []
    for item in data:
        pack = {
            "name": item[0],
            "color": item[1],
            "features": format_as_list(item[2]),
            "like": format_as_list(item[3]),
            "dislike": format_as_list(item[4]),
            "birth": item[5],
            "sex": item[6],
            "castrated": format_cast(item[7]),
            "rip": False,
            "relation": item[8],
            "code": manage_code
        }
        data_pack_list.append(pack)
    return data_pack_list


class ProfileData(BaseModel):
    name: str
    color: str
    features: list
    like: list
    dislike: list
    birth: str
    sex: str
    castrated: bool
    rip: bool
    relation: str
    code: str


def make_pack_new(data):
    data_pack_list = []
    for item in data:
        data_pack_list.append(ProfileData(
            name=item[0],
            color=item[1],
            features=format_as_list(item[2]),
            like=format_as_list(item[3]),
            dislike=format_as_list(item[4]),
            birth=item[5],
            sex=item[6],
            castrated=format_cast(item[7]),
            rip=False,
            relation=item[8],
            code=manage_code
        ).dict())
    return data_pack_list


def update():
    resp_list = []
    for item in make_pack_new(load()):
        resp = send(item)
        print(resp)
        resp_list.append(resp)

    with open("./a.json", "w") as f:
        f.write(json.dumps(resp_list))


update()


# print(make_pack(load()))
# a = new_fake()
# # search()
# with open("./a.json", "w") as f:
#     f.write(json.dumps(a))
