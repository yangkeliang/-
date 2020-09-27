import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.decorate as de
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.geturl("获取标签列表",0)
@de.prt
def test_01_gettagelist_success_tag0(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    sql = "select count(*) from (SELECT tags FROM t_content_tags\
           WHERE ctype = {} AND STATUS = 0\
           GROUP BY tags) a;".format(url[-1])
    assert len(res.json()["data"]["tags"].split(",")) == db.query(sql)[0][0]
    return res

@de.geturl("获取标签列表",1)
@de.prt
def test_01_gettagelist_success_tag1(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    sql = "select count(*) from (SELECT tags FROM t_content_tags\
           WHERE ctype = {} AND STATUS = 0\
           GROUP BY tags) a;".format(url[-1])
    assert len(res.json()["data"]["tags"].split(",")) == db.query(sql)[0][0]
    return res

@de.geturl("获取标签列表",2)
@de.prt
def test_01_gettagelist_success_tag3(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    sql = "select count(*) from (SELECT tags FROM t_content_tags\
           WHERE ctype = {} AND STATUS = 0\
           GROUP BY tags) a;".format(url[-1])
    assert len(res.json()["data"]["tags"].split(",")) == db.query(sql)[0][0]
    return res

@de.geturl("获取标签列表",3)
@de.prt
def test_01_gettagelist_fail_tagnotexist(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "标签为0，1，3"
    return res

@de.geturl("获取标签列表",4)
@de.prt
def test_01_gettagelist_fail_tagchar(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "标签为0，1，3"
    return res

@de.geturl("获取标签列表",5)
@de.prt
def test_01_gettagelist_fail_tagnull(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "标签不可为空"
    return res

@de.geturl("获取标签列表",6)
@de.prt
def test_01_gettagelist_fail_tagxiaoshu(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "标签为0，1，3"
    return res