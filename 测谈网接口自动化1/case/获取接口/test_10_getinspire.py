import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de
@de.outer
def test_01_getinspire_success():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取灵感")
    url = e_data[0][2]
    head = eval(e_data[0][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert len(res.json()["data"]["contentlist"]) == 10#返回10条
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res

def test_02_getinspire_noparameter():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取灵感")
    url = e_data[1][2]
    head = eval(e_data[1][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert len(res.json()["data"]) == 4 
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码

def test_03_getinspire_paraxiaoshu():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取灵感")
    url = e_data[2][2]
    head = eval(e_data[2][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1]) 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码

def test_04_getinspire_parachar():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取灵感")
    url = e_data[3][2]
    head = eval(e_data[3][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(url.split("=")[1]) 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码

def test_05_getinspire_parafushu():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取灵感")
    url = e_data[4][2]
    head = eval(e_data[4][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["msg"] == "数字必须大于0" 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码

def test_06_getinspire_paranotexist():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取灵感")
    url = e_data[5][2]
    head = eval(e_data[5][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["msg"] == "页码超出范围" 
    assert res.json()["status"] == 401#状态码
    assert res.status_code == 200#结果码