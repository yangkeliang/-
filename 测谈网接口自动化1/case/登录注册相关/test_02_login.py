import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.prt
@de.posturl("登录",0)
def test_01_login_success(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "登录成功！"
    return res

@de.prt
@de.posturl("登录",1)
def test_02_login_shortname(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"
    return res
     
@de.prt
@de.posturl("登录",2)
def test_03_login_longname(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"
    return res
     
@de.prt
@de.posturl("登录",3)
def test_04_login_namenotexsit(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "用户名未注册"
    return res
     
@de.prt
@de.posturl("登录",4)
def test_05_login_paswrong(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "密码错误"
    return res
     
@de.prt
@de.posturl("登录",5)
def test_06_login_usernamenull(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号名不能为空"
    return res

@de.prt
@de.posturl("登录",6)
def test_07_login_passnull(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "密码不能为空"
    return res
     
