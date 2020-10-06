import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de


@de.prt
@de.geturl("获取热门文章",0)
def test_01_getarticle_success(res,url,head):
    assert len(res.json()["data"]["contentlist"]) == 10#返回10条
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res
     


@de.prt
@de.geturl("获取热门文章",1)
def test_02_getarticle_noparameter(res,url,head):
    assert len(res.json()["data"]) == 4 
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res
     


@de.prt
@de.geturl("获取热门文章",2)
def test_03_getarticle_paraxiaoshu(res,url,head):
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1]) 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res


@de.prt
@de.geturl("获取热门文章",3)
def test_04_getarticle_parachar(res,url,head):
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1]) 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res


@de.prt
@de.geturl("获取热门文章",4)
def test_05_getarticle_parafushu(res,url,head):
    assert res.json()["msg"] == "数字必须大于0" 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res


@de.prt
@de.geturl("获取热门文章",5)
def test_06_getarticle_paranotexist(res,url,head):
    assert res.json()["msg"] == "页码超出范围" 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    return res