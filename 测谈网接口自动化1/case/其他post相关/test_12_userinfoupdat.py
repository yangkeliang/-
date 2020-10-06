import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de
import case.登录注册相关.test_02_login as te
import utils.gettoken as to
import utils.getid as ge

@de.prt
@de.posturl("修改个人资料接口",0)
def test_01_userinfoup_successmale(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == True
    return res

@de.prt
@de.posturl("修改个人资料接口",1)
def test_02_userinfoup_successfemale(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == True
    return res

@de.prt
@de.posturl("修改个人资料接口",2)
def test_03_userinfoup_successsecret(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == True
    return res

@de.prt
@de.posturl("修改个人资料接口",3)
def test_04_userinfoup_failphonewrong(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "手机格式不对！"
    return res

@de.prt
@de.posturl("修改个人资料接口",4)
def test_05_userinfoup_failphonesame(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "电话已经注册，请重新设置！"
    return res

@de.prt
@de.posturl("修改个人资料接口",5)
def test_06_userinfoup_failphonenull(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "手机格式不对！"
    return res

@de.prt
@de.posturl("修改个人资料接口",6)
def test_07_userinfoup_failphonenull(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "邮箱格式不对！"
    return res

@de.prt
@de.posturl("修改个人资料接口",7)
def test_08_userinfoup_failphonenull(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "邮箱格式不对！"
    return res

@de.prt
@de.posturl("修改个人资料接口",8)
def test_09_userinfoup_gendernull(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["data"] == "性别只能是男、女、保密"
    return res

@de.prt
@de.posturl("修改个人资料接口",9)
def test_10_userinfoup_genderwrong(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["data"] == "性别只能是男、女、保密"
    return res