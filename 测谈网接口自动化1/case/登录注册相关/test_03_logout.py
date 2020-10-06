import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de
import case.登录注册相关.test_02_login as te
import utils.gettoken as to

@de.prt
@de.geturl("用户退出登录接口",0)
def test_01_logout_success(res,url,head):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.get(url=url,headers=head)#重新get
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "退出成功！"
    return res
     