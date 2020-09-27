import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.decorate as de
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.geturl("获取用户动态列表",0)
@de.prt
def test_01_userdt_success(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["userlist"]) != 0
    return res

@de.geturl("获取用户动态列表",1)
@de.prt
def test_02_userdt_fail_uidnotexsit(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["userlist"]) == 0
    return res

@de.geturl("获取用户动态列表",2)
@de.prt
def test_03_userdt_fail_uidnull(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "不能为空"
    return res

@de.geturl("获取用户动态列表",3)
@de.prt
def test_04_userdt_fail_uidchar(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1].split("&")[0])
    return res

@de.geturl("获取用户动态列表",4)
@de.prt
def test_05_userdt_fail_pagebig(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["userlist"]) == 0
    return res

@de.geturl("获取用户动态列表",5)
@de.prt
def test_06_userdt_fail_pagenull(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "不能为空"
    return res

@de.geturl("获取用户动态列表",6)
@de.prt
def test_07_userdt_fail_pagechar(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[2])
    return res

@de.geturl("获取用户动态列表",7)
@de.prt
def test_08_userdt_fail_pagexiaoshu(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[2])
    return res