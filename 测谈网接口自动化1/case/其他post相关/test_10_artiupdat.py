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
@de.posturl("用户修改文章接口",0)
def test_01_artup_success(res,url,head,body):
    aid = ge.getaid()
    body["aid"] = aid#qid重新赋值
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == True
    return res

@de.prt
@de.posturl("用户修改文章接口",1)
def test_02_artup_fail_tag3(res,url,head,body):
    aid = ge.getaid()
    body["aid"] = aid#qid重新赋值
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "每个标签要求不能大于6个字，不能少于4个字。"
    return res

@de.prt
@de.posturl("用户修改文章接口",2)
def test_03_artup_fail_tag7(res,url,head,body):
    qid = ge.getqid()
    body["qid"] = qid#qid重新赋值
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "每个标签要求不能大于6个字，不能少于4个字。"
    return res

@de.prt
@de.posturl("用户修改文章接口",3)
def test_04_artup_fail_idchar(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "【{}】应该是正整数才行！".format(body["aid"])
    return res

@de.prt
@de.posturl("用户修改文章接口",4)
def test_05_artup_fail_idxioashu(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "修改的文章不存在！"
    return res

@de.prt
@de.posturl("用户修改文章接口",5)
def test_06_artup_fail_fushu(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "数字必须大于0"
    return res