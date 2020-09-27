import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.decorate as de
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.geturl("搜索",0)
@de.prt
def test_01_search_success_type0(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) != 0
    return res

@de.geturl("搜索",1)
@de.prt
def test_02_search_fail_type0_notfound(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) == 0
    return res

@de.geturl("搜索",2)
@de.prt
def test_03_search_fail_type0_pagebig(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "页码数超出范围"
    return res

@de.geturl("搜索",3)
@de.prt
def test_04_search_fail_type0_pagenull(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入页码"
    return res

@de.geturl("搜索",4)
@de.prt
def test_05_search_fail_type0_typenull(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入类型"
    return res

@de.geturl("搜索",5)
@de.prt
def test_06_search_fail_type0_valuenull(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入搜索值"
    return res

@de.geturl("搜索",6)
@de.prt
def test_07_search_fail_typenull(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入类型"
    return res

@de.geturl("搜索",7)
@de.prt
def test_08_search_success_type1(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) != 0
    return res

@de.geturl("搜索",8)
@de.prt
def test_09_search_success_type1(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) != 0
    return res

@de.geturl("搜索",9)
@de.prt
def test_10_search_success_type1(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) != 0
    return res

@de.geturl("搜索",10)
@de.prt
def test_11_search_success_type1(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) != 0
    return res