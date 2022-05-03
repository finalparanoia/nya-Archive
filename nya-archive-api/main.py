import fastapi
import uvicorn
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from libs.bll import BusinessLogicLayer


manage_code = "77807aa2f1fcf812544660ea5923fbd33076b9154cb67fef3b7ed7289ff85b82"


app = fastapi.FastAPI()
bll = BusinessLogicLayer()


# 允许跨域
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# 触发异常
def fail(code: int, info: str):
    raise fastapi.HTTPException(status_code=code, detail=info)


# 测试服务器是否开启
@app.get("/test/")
async def test_api():
    return {"status_code": 0}


# 根据nid查询猫猫信息
@app.get("/check/{nid}")
async def check_api(nid: str):
    resp = bll.check(nid)
    if not resp:
        fail(404, "没有找到对应的猫喵~")
    else:
        return resp


# 查询的类
class SearchData(BaseModel):
    name: Optional[str] = ""
    color: Optional[str] = ""


# 查询接口
@app.post("/search/")
async def search_api(data: SearchData):
    resp = bll.search(data.dict())
    if not resp:
        fail(404, "一直符合要求的猫猫都没有喵~")
    else:
        return resp


# 档案类
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


# 添加档案接口
@app.post("/add/")
async def search_api(data: ProfileData):
    print(data.dict())
    if data.code == manage_code:
        resp = bll.new(data.dict())
        if not resp:
            fail(404, "已经由对应的猫猫了喵~")
        else:
            return resp
    else:
        fail(401, "没有访问权限喵~")

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=9888, reload=True)
