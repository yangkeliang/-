import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.decorate as de
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de


@de.prt
@de.geturl("获取用户问题列表",0)
def test_01_userquestion_success(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) != 0
    return res


@de.prt
@de.geturl("获取用户问题列表",1)
def test_02_userquestion_fail_uidnotexsit(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) == 0
    return res


@de.prt
@de.geturl("获取用户问题列表",2)
def test_03_userquestion_fail_uidnull(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "不能为空"
    return res


@de.prt
@de.geturl("获取用户问题列表",3)
def test_04_userquestion_fail_uidchar(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1].split("&")[0])
    return res


@de.prt
@de.geturl("获取用户问题列表",4)
def test_05_userquestion_fail_pagebig(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]["contentlist"]) == 0
    return res


@de.prt
@de.geturl("获取用户问题列表",5)
def test_06_userquestion_fail_pagenull(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "不能为空"
    return res


@de.prt
@de.geturl("获取用户问题列表",6)
def test_07_userquestion_fail_pagechar(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[2])
    return res


@de.prt
@de.geturl("获取用户问题列表",7)
def test_08_userquestion_fail_pagexiaoshu(res,url,head):
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[2])
    return res