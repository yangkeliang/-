import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.decorate as de
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de


@de.prt
@de.geturl("获取用户粉丝列表",0)
def test_01_userfans_success_type0(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    sql = "select * from t_user where id ={}".format(url.split("=")[1])
    assert len(db.query(sql)) ==1
    return res


@de.prt
@de.geturl("获取用户粉丝列表",1)
def test_02_userfans_fail_uidnull(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "不能为空"
    return res


@de.prt
@de.geturl("获取用户粉丝列表",2)
def test_03_userfans_fail_uidxiaoshu(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1])
    return res     


@de.prt
@de.geturl("获取用户粉丝列表",3)
def test_04_userfans_fail_uidchar(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1])
    return res


@de.prt
@de.geturl("获取用户粉丝列表",4)
def test_05_userfans_fail_uidnotexsist(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["userlist"]) == 0
    return res