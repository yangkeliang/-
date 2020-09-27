import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.decorate as de
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.geturl("获取用户关注人列表",0)
@de.prt
def test_01_userfollower_success_type0(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    sql = "select * from t_user where id ={}".format(url.split("=")[1])
    assert len(db.query(sql)) ==1
    return res

@de.geturl("获取用户关注人列表",1)
@de.prt
def test_02_userfollower_fail_uidnull(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "不能为空"
    return res

@de.geturl("获取用户关注人列表",2)
@de.prt
def test_03_userfollower_fail_uidxiaoshu(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1])
    return res

@de.geturl("获取用户关注人列表",3)
@de.prt
def test_04_userfollower_fail_uidchar(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1])
    return res

@de.geturl("获取用户关注人列表",4)
@de.prt
def test_05_userfollower_fail_uidnotexsist(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["userlist"]) == 0
    return res