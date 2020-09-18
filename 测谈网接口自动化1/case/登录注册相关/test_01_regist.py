import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
def test_01_regist_wrongname():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[0][2]
    head = eval(e_data[0][5])
    data = eval(e_data[0][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号仅能由数字和小写字母组成！"
def test_02_regist_fail_wrongphone():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[1][2]
    head = eval(e_data[1][5])
    data = eval(e_data[1][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "请输入正确的手机号！"
def test_03_regist_fail_shortname():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[2][2]
    head = eval(e_data[2][5])
    data = eval(e_data[2][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"
def test_04_regist_fail_longname():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[3][2]
    head = eval(e_data[3][5])
    data = eval(e_data[3][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"
def test_05_regist_fail_nophone():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[4][2]
    head = eval(e_data[4][5])
    data = eval(e_data[4][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "输入的参数不能有空值！"
def test_06_regist_fail_wrongmail():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[5][2]
    head = eval(e_data[5][5])
    data = eval(e_data[5][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "请输入正确的邮箱！"
def test_07_regist_fail_noname():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[6][2]
    head = eval(e_data[6][5])
    data = eval(e_data[6][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "输入的参数不能有空值！"
def test_08_regist_fail_nomail():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[7][2]
    head = eval(e_data[7][5])
    data = eval(e_data[7][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "输入的参数不能有空值！"
def test_08_regist_fail_nopasswd():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[8][2]
    head = eval(e_data[8][5])
    data = eval(e_data[8][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "输入的参数不能有空值！"
def test_09_regist_fail_shortpasswd():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[9][2]
    head = eval(e_data[9][5])
    data = eval(e_data[9][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "密码长度必须大于等于8位，并且小于等于16位"
def test_10_regist_fail_longpasswd():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[10][2]
    head = eval(e_data[10][5])
    data = eval(e_data[10][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "密码长度必须大于等于8位，并且小于等于16位"
def test_11_regist_success():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[11][2]
    head = eval(e_data[11][5])
    data = eval(e_data[11][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select * from t_user where username = '{}'".format(data["username"])
    assert len(db.query(sql)) != 0
def test_12_regist_fail_nameexsist():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[12][2]
    head = eval(e_data[12][5])
    data = eval(e_data[12][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "用户名已存在，请重新设置！"
def test_13_regist_fail_phoneexsist():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[13][2]
    head = eval(e_data[13][5])
    data = eval(e_data[13][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "电话已经注册，请重新设置！"
def test_14_regist_fail_mailexsist():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "用户注册")
    url = e_data[14][2]
    head = eval(e_data[14][5])
    data = eval(e_data[14][4])
    res = requests.post(url=url,headers=head,json=data)#head中规定使用json，因此用json而不是data
    assert res.status_code == 200
    assert res.json()["status"] ==  401
    assert res.json()["msg"] == "邮箱已经注册，请重新设置！"