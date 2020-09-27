import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.exceltools as extool
import utils.dbtools as  db
import utils.decorate as de

@de.posturl("登录",0)
@de.prt
def test_01_login_success(res,url,head,body):
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 200#结果码
    sql = "select * from t_user where username = '{}'".format(body["username"])
    assert len(db.query(sql)) != 0#判断数据库
    return res

@de.posturl("登录",1)
@de.prt
def test_02_login_fail_shortname(res,url,head,body):
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"#结果码
    return res

@de.posturl("登录",2)
@de.prt
def test_03_login_fail_longname(res,url,head,body):
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"#结果码
    return res
    '''服务器无法重复三次以上访问同一接口'''