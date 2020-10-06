import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de
import case.登录注册相关.test_02_login as te

@de.prt
@de.posturl("找回密码",0)
def test_01_userfindps_success(res,url,head,body):
    assert res.json()["status"] ==200
    assert res.status_code ==200
    assert res.json()["msg"] =="设置新密码成功！"
    e_data1 = extool.read_excel("data/测谈网接口测试用例.xlsx", "找回密码")
    head1 = eval(e_data1[0][5])#从找回密码中读head
    body1 = eval(e_data1[0][4])#从找回密码中读body
    mb = body1.pop("mb")#改造body
    e_data2 = extool.read_excel("data/测谈网接口测试用例.xlsx", "登录")
    url2 = e_data2[0][2]
    res2 = requests.post(url=url2,headers=head1,json=body1)#看更改后的接口是否可以登录成功
    assert res2.json()["msg"] =="登录成功！"
    body1["mb"] = mb#恢复body
    body1["password"] = "a1234567"
    res3 = requests.post(url=url,headers=head,json=body1)#把密码改回去
    return res


@de.prt
@de.posturl("找回密码",1)
def test_02_userfindps_passwdlong(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密码长度必须大于等于8位，并且小于等于16位"
    return res
     


@de.prt
@de.posturl("找回密码",2)
def test_03_userfindps_passwdshort(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密码长度必须大于等于8位，并且小于等于16位"
    return res
     


@de.prt
@de.posturl("找回密码",3)
def test_04_userfindps_passwdnull(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密码不能为空！"
    return res
     


@de.prt
@de.posturl("找回密码",4)
def test_05_userfindps_namenotexist(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="账号不存在！"
    return res
     


@de.prt
@de.posturl("找回密码",5)
def test_06_userfindps_mb1null(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密保错误！"
    return res
     


@de.prt
@de.posturl("找回密码",6)
def test_07_userfindps_mb2null(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密保错误！"
    return res
     


@de.prt
@de.posturl("找回密码",7)
def test_08_userfindps_mb3null(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密保错误！"
    return res


@de.prt
@de.posturl("找回密码",8)
def test_09_userfindps_mb1erro(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密保错误！"
    return res
     


@de.prt
@de.posturl("找回密码",9)
def test_10_userfindps_mb2null(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密保错误！"
    return res
     


@de.prt
@de.posturl("找回密码",10)
def test_11_userfindps_mb3null(res,url,head,body):
    assert res.json()["status"] ==401
    assert res.status_code ==200
    assert res.json()["msg"] =="密保错误！"
    return res
     