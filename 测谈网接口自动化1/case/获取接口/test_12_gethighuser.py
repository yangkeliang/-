import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.geturl("获取活跃用户",0)
@de.prt
def test_01_gethighusers_success(res,url,head):
    assert len(res.json()["data"]) ==15#返回15条
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res

@de.geturl("获取活跃用户",1)
@de.prt
def test_02_gethighusers_noparameter(res,url,head):
    assert len(res.json()["data"]) == 15 
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res

@de.geturl("获取活跃用户",2)
@de.prt
def test_03_gethighusers_paraxiaoshu(res,url,head):
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1]) 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res

@de.geturl("获取活跃用户",3)
@de.prt
def test_04_gethighusers_parachar(res,url,head):
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1]) 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res

@de.geturl("获取活跃用户",4)
@de.prt
def test_05_gethighusers_parafushu(res,url,head):
    assert res.json()["msg"] == "数字必须大于0" 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res

@de.geturl("获取活跃用户",5)
@de.prt
def test_06_gethighusers_paranotexist(res,url,head):
    assert res.json()["msg"] == "操作成功！" 
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res