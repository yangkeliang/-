import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
def test_01_getarticledetail_success():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取文章详情")
    url = e_data[0][2]
    head = eval(e_data[0][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    assert len(res.json()["data"]) != 0
    

def test_02_getarticledetail_fail_xiaoshu():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取文章详情")
    url = e_data[1][2]
    head = eval(e_data[1][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"

def test_03_getarticledetail_fail_fushu():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取文章详情")
    url = e_data[2][2]
    head = eval(e_data[2][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"

def test_04_getarticledetail_fail_zifu():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取文章详情")
    url = e_data[3][2]
    head = eval(e_data[3][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"

def test_05_getarticledetail_fail_char():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取文章详情")
    url = e_data[4][2]
    head = eval(e_data[4][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"

def test_06_getarticledetail_fail_null():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取文章详情")
    url = e_data[5][2]
    head = eval(e_data[5][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"

def test_07_getarticledetail_fail_notexist():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取文章详情")
    url = e_data[6][2]
    head = eval(e_data[6][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码
    assert res.json()["msg"] == "请输入正整数"