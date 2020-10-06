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
@de.posturl("收藏取消收藏接口接口",0)
def test_01_fellcollectype0_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "收藏成功！"#先收藏
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消收藏成功！"#再取消收藏
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",1)
def test_02_fellcollectype1_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "收藏成功！"#先收藏
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消收藏成功！"#再取消收藏
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",2)
def test_03_fellcollectype2_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "收藏成功！"#先收藏
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消收藏成功！"#再取消收藏
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",3)
def test_04_fellcollectype3_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "收藏成功！"#先收藏
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消收藏成功！"#再取消收藏
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",4)
def test_05_fellcollectypenull_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "ctype类型不对"
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",5)
def test_06_fellcollectypewrong_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "ctype类型不对"
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",6)
def test_07_fellcollectype0notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该教程"
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",7)
def test_08_fellcollectype1notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该问题"
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",8)
def test_09_fellcollectype2notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该灵感"
    return res

@de.prt
@de.posturl("收藏取消收藏接口接口",9)
def test_10_fellcollectype3notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该文章"
    return res