import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.geturl("获取文章详情",0)
@de.prt
def test_01_getarticledetail_success(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]) != 0
    return res
    
@de.geturl("获取文章详情",1)
@de.prt
def test_02_getarticledetail_fail_xiaoshu(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"
    return res

@de.geturl("获取文章详情",2)
@de.prt
def test_03_getarticledetail_fail_fushu(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"
    return res

@de.geturl("获取文章详情",3)
@de.prt
def test_04_getarticledetail_fail_zifu(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"
    return res

@de.geturl("获取文章详情",4)
@de.prt
def test_05_getarticledetail_fail_char(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"
    return res

@de.geturl("获取文章详情",5)
@de.prt
def test_06_getarticledetail_fail_null(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"
    return res

@de.geturl("获取文章详情",6)
@de.prt
def test_07_getarticledetail_fail_notexist(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"
    return res