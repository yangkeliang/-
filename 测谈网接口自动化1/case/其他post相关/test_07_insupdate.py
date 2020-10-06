import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de
import utils.gettoken as to
import utils.getid as ge

@de.prt
@de.posturl("用户修改灵感接口",0)
def test_01_insup_success(res,url,head,body):
    iid = ge.getiid()
    body["iid"] = iid#qid重新赋值
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == True
    return res

@de.prt
@de.posturl("用户修改灵感接口",1)
def test_02_insup_fail_notexsist(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "修改的灵感不存在！"
    return res

@de.prt
@de.posturl("用户修改灵感接口",2)
def test_03_insup_fail_idchar(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(body["iid"])
    return res

@de.prt
@de.posturl("用户修改灵感接口",3)
def test_04_queup_fail_idxiaoshu(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "修改的灵感不存在！"
    return res

@de.prt
@de.posturl("用户修改灵感接口",4)
def test_05_queup_fail_idfushu(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "数字必须大于0"
    return res