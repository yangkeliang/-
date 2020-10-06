import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.prt
@de.posturl("用户注册",0)
def test_01_regist_wrongname(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号仅能由数字和小写字母组成！"
    return res
     
@de.prt
@de.posturl("用户注册",1)
def test_02_regist_fail_wrongphone(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "请输入正确的手机号！"
    return res
     
@de.prt
@de.posturl("用户注册",2)
def test_03_regist_fail_shortname(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"
    return res
     
@de.prt
@de.posturl("用户注册",3)
def test_04_regist_fail_longname(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "账号长度必须大于等于5位，并且小于等于12位"
    return res
     
@de.prt    
@de.posturl("用户注册",4)
def test_05_regist_fail_nophone(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "输入的参数不能有空值！"
    return res
     
@de.prt
@de.posturl("用户注册",5)
def test_06_regist_fail_wrongmail(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "请输入正确的邮箱！"
    return res
     
@de.prt
@de.posturl("用户注册",6)
def test_07_regist_fail_noname(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "输入的参数不能有空值！"
    return res
     
@de.prt
@de.posturl("用户注册",7)
def test_08_regist_fail_nomail(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "输入的参数不能有空值！"
    return res
     
@de.prt
@de.posturl("用户注册",8)
def test_08_regist_fail_nopasswd(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "输入的参数不能有空值！"
    return res
     
@de.prt
@de.posturl("用户注册",9)
def test_09_regist_fail_shortpasswd(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "密码长度必须大于等于8位，并且小于等于16位"
    return res
     
@de.prt
@de.posturl("用户注册",10)
def test_10_regist_fail_longpasswd(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "密码长度必须大于等于8位，并且小于等于16位"
    return res
     
@de.prt
@de.posturl("用户注册",11)
def test_11_regist_success(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select * from t_user where username = '{}'".format(body["username"])
    assert len(db.query(sql)) != 0
    return res
     
@de.prt
@de.posturl("用户注册",12)
def test_12_regist_fail_nameexsist(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "用户名已存在，请重新设置！"
    return res
     
@de.prt
@de.posturl("用户注册",13)
def test_13_regist_fail_phoneexsist(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] == 401
    assert res.json()["msg"] == "电话已经注册，请重新设置！"
    return res
     
@de.prt
@de.posturl("用户注册",14)
def test_14_regist_fail_mailexsist(res,url,head,body):
    assert res.status_code == 200
    assert res.json()["status"] ==  401
    assert res.json()["msg"] == "邮箱已经注册，请重新设置！"
    return res
     