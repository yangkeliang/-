import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.prt
@de.geturl("获取推荐教程",0)
def test_01_getcourse_success(res,url,head):
    assert len(res.json()["data"]["contentlist"]) == 10#返回10条
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res
     
@de.prt
@de.geturl("获取推荐教程",1)
def test_02_getcourse_noparameter(res,url,head):
    assert len(res.json()["data"]) == 3 
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res
     
@de.prt
@de.geturl("获取推荐教程",2)
def test_03_getcourse_paraxiaoshu(res,url,head):
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1]) 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res
     
@de.prt
@de.geturl("获取推荐教程",3)
def test_04_getcourse_parachar(res,url,head):
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1]) 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res
     
@de.prt
@de.geturl("获取推荐教程",4)
def test_05_getcourse_parafushu(res,url,head):
    assert res.json()["msg"] == "数字必须大于0" 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res
     
@de.prt
@de.geturl("获取推荐教程",5)
def test_06_getcourse_paranotexist(res,url,head):
    assert res.json()["msg"] == "页码超出范围" 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res
     