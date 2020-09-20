import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de
       
@de.outer
def test_01_getcomment_success_type0():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[0][4]) 
    url = excel[0][2]
    head = eval(excel[0][5])
    res = requests.post(url=url,headers=head,json=data)
    #判断数据量是否相等
    sqlcount = "SELECT count(*) FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(data["ctype"],data["fid"],10*(int(data["pagenum"])-1))
    num = db.query(sqlcount)[0][0]
    assert num == res.json()["data"]["counts"]#判断数据量是否相等
    assert len(res.json()["data"]["contentlist"]) == 10 or len(res.json()["data"]["contentlist"]) == num#判断每页数量是否为10，小于10是否为数据库中总数
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "SELECT comment FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(data["ctype"],data["fid"],10*(int(data["pagenum"])-1))
    numle = num%10#第一页第几个，如果总数大于10，取余数，总数小于10，取本身
    assert num ==0 or db.query(sql)[numle-1][0] == res.json()["data"]["contentlist"][numle-1]["comment"]#查到的最后一个元素是否相同
    return res

@de.outer
def test_01_getcomment_success_type1():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[1][4]) 
    url = excel[1][2]
    head = eval(excel[1][5])
    res = requests.post(url=url,headers=head,json=data)
    #判断数据量是否相等
    sqlcount = "SELECT count(*) FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(data["ctype"],data["fid"],10*(int(data["pagenum"])-1))
    num = db.query(sqlcount)[0][0]
    assert num == res.json()["data"]["counts"]#判断数据量是否相等
    assert len(res.json()["data"]["contentlist"]) == 10 or len(res.json()["data"]["contentlist"]) == num#判断每页数量是否为10，小于10是否为数据库中总数
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "SELECT comment FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(data["ctype"],data["fid"],10*(int(data["pagenum"])-1))
    numle = num%10#第一页第几个，如果总数大于10，取余数，总数小于10，取本身
    assert num == 10 or db.query(sql)[numle-1][0] == res.json()["data"]["contentlist"][numle-1]["comment"]#查到的最后一个元素是否相同
    return res

@de.outer
def test_01_getcomment_success_type2():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[2][4]) 
    url = excel[2][2]
    head = eval(excel[2][5])
    res = requests.post(url=url,headers=head,json=data)
    #判断数据量是否相等
    sqlcount = "SELECT count(*) FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(data["ctype"],data["fid"],10*(int(data["pagenum"])-1))
    num = db.query(sqlcount)[0][0]
    assert num == res.json()["data"]["counts"]#判断数据量是否相等
    assert len(res.json()["data"]["contentlist"]) == 10 or len(res.json()["data"]["contentlist"]) == num#判断每页数量是否为10，小于10是否为数据库中总数
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "SELECT comment FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(data["ctype"],data["fid"],10*(int(data["pagenum"])-1))
    numle = num%10#第一页第几个，如果总数大于10，取余数，总数小于10，取本身
    assert num == 0 or db.query(sql)[numle-1][0] == res.json()["data"]["contentlist"][numle-1]["comment"] #查到的最后一个元素是否相同
    return res

@de.outer
def test_01_getcomment_success_type3():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[3][4]) 
    url = excel[3][2]
    head = eval(excel[3][5])
    res = requests.post(url=url,headers=head,json=data)
    #判断数据量是否相等
    sqlcount = "SELECT count(*) FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(data["ctype"],data["fid"],10*(int(data["pagenum"])-1))
    num = db.query(sqlcount)[0][0]
    assert num == res.json()["data"]["counts"]#判断数据量是否相等
    assert len(res.json()["data"]["contentlist"]) == 10 or len(res.json()["data"]["contentlist"]) == num#判断每页数量是否为10，小于10是否为数据库中总数
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "SELECT comment FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(data["ctype"],data["fid"],10*(int(data["pagenum"])-1))
    numle = num%10#第一页第几个，如果总数大于10，取余数，总数小于10，取本身
    assert num == 0 or db.query(sql)[numle-1][0] == res.json()["data"]["contentlist"][numle-1]["comment"] #查到的最后一个元素是否相同
    return res

@de.outer
def test_01_getcomment_fail_typenotexist():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[4][4]) 
    url = excel[4][2]
    head = eval(excel[4][5])
    res = requests.post(url=url,headers=head,json=data)
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 401#结果码
    assert res.json()["msg"] == "ctypectype不在范围内，0教程1提问2灵感3心得体会"#提示信息
    return res

@de.outer
def test_01_getcomment_fail_fidnotint():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[5][4]) 
    url = excel[5][2]
    head = eval(excel[5][5])
    res = requests.post(url=url,headers=head,json=data)
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 401#结果码
    assert res.json()["msg"] == "fid【{}】应该是正整数才行！".format(data["fid"])#提示信息
    return res

@de.outer
def test_01_getcomment_fail_fidnull():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[6][4]) 
    url = excel[6][2]
    head = eval(excel[6][5])
    res = requests.post(url=url,headers=head,json=data)
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "fid不能为空"#提示信息
    return res

@de.outer
def test_01_getcomment_fail_ctypenull():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[7][4]) 
    url = excel[7][2]
    head = eval(excel[7][5])
    res = requests.post(url=url,headers=head,json=data)
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "ctypectype不在范围内，0教程1提问2灵感3心得体会"#提示信息
    return res

@de.outer
def test_01_getcomment_fail_pagenull():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[8][4]) 
    url = excel[8][2]
    head = eval(excel[8][5])
    res = requests.post(url=url,headers=head,json=data)
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "pagenum不能为空"#提示信息
    return res

@de.outer
def test_01_getcomment_fail_pagetoobig():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[9][4]) 
    url = excel[9][2]
    head = eval(excel[9][5])
    res = requests.post(url=url,headers=head,json=data)
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "页码超出范围"#提示信息
    return res

@de.outer
def test_01_getcomment_fail_pagexiaoshu():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[10][4]) 
    url = excel[10][2]
    head = eval(excel[10][5])
    res = requests.post(url=url,headers=head,json=data)
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "pagenum【{}】应该是正整数才行！".format(data["pagenum"])#提示信息
    return res

@de.outer
def test_01_getcomment_fail_pagechar():
    excel = extool.read_excel("data/测谈网接口测试用例.xlsx","获取评论列表")
    data = eval(excel[11][4]) 
    url = excel[11][2]
    head = eval(excel[11][5])
    res = requests.post(url=url,headers=head,json=data)
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "pagenum【{}】应该是正整数才行！".format(data["pagenum"])#提示信息
    return res