import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as  db
import time
def test_01_login_success():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "登录")
    url = e_data[0][2]
    head = eval(e_data[0][5])
    body = eval(e_data[0][4])
    res = requests.post(url=url,headers=head,json=body)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 200#结果码
    sql = "select * from t_user where username = '{}'".format(body["username"])
    assert len(db.query(sql)) != 0#判断数据库
def test_02_login_fail_shortname():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "登录")
    url = e_data[1][2]
    head = eval(e_data[1][5])
    body = eval(e_data[1][4])
    res = requests.post(url=url,headers=head,json=body)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"#结果码
def test_03_login_fail_longname():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "登录")
    url = e_data[2][2]
    head = eval(e_data[2][5])
    body = eval(e_data[2][4])
    res = requests.post(url=url,headers=head,json=body)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"#结果码

    '''服务器无法重复三次以上访问同一接口'''