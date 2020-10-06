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
@de.posturl("点赞取消点赞接口接口",0)
def test_01_fellgoodctype0_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "点赞成功！"#先点赞
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消点赞成功！"#再取消点赞
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",1)
def test_02_fellgoodctype1_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "点赞成功！"#先点赞
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消点赞成功！"#再取消点赞
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",2)
def test_03_fellgoodctype2_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "点赞成功！"#先点赞
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消点赞成功！"#再取消点赞
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",3)
def test_04_fellgoodctype3_success(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["msg"] == "点赞成功！"#先点赞
    res1 = requests.post(url=url,headers=head,json=body)#重新post
    assert res1.status_code == 200
    assert res1.json()["status"] == 200
    assert res1.json()["msg"] == "取消点赞成功！"#再取消点赞
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",4)
def test_05_fellgoodctypenull_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "ctype类型不正确！"
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",5)
def test_06_fellgoodctypewrong_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "ctype类型不正确！"
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",6)
def test_07_fellgoodctype0notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该教程"
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",7)
def test_08_fellgoodctype1notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该问题"
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",8)
def test_09_fellgoodctype2notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该灵感"
    return res

@de.prt
@de.posturl("点赞取消点赞接口接口",9)
def test_10_fellgoodctype3notexsist_fail(res,url,head,body):
    token = to.getoken()#获得token
    head["token"] = token#token重新赋值
    res = requests.post(url=url,headers=head,json=body)#重新post
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "不存在该文章"
    return res