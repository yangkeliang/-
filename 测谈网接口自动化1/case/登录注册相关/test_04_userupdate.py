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
@de.posturl("用户修改密码接口",0)
def test_01_update_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "密码修改成功！请重新登录！"
    old = body["oldps"]
    new = body["newps"]
    body["oldps"] = new
    body["newps"] = old#重置密码
    res = requests.post(url=url,headers=head,json=body)
    return res

@de.prt
@de.posturl("用户修改密码接口",1)
def test_02_update_fail_oldwrong(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "旧密码不正确！"
    return res

@de.prt
@de.posturl("用户修改密码接口",2)
def test_03_fail_newnotright(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401
    return res


     