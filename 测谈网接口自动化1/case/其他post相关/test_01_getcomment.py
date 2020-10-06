import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de
       

@de.prt
@de.posturl("获取评论列表",0)
def test_01_getcomment_success_type0(res,url,head,body):
    #判断数据量是否相等
    sqlcount = "SELECT count(*) FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(body["ctype"],body["fid"],10*(int(body["pagenum"])-1))
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
            DESC LIMIT {},10;".format(body["ctype"],body["fid"],10*(int(body["pagenum"])-1))
    numle = num%10#第一页第几个，如果总数大于10，取余数，总数小于10，取本身
    assert num ==0 or db.query(sql)[numle-1][0] == res.json()["data"]["contentlist"][numle-1]["comment"]#查到的最后一个元素是否相同
    return res


@de.prt
@de.posturl("获取评论列表",1)
def test_01_getcomment_success_type1(res,url,head,body):
    #判断数据量是否相等
    sqlcount = "SELECT count(*) FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(body["ctype"],body["fid"],10*(int(body["pagenum"])-1))
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
            DESC LIMIT {},10;".format(body["ctype"],body["fid"],10*(int(body["pagenum"])-1))
    numle = num%10#第一页第几个，如果总数大于10，取余数，总数小于10，取本身
    assert num == 10 or db.query(sql)[numle-1][0] == res.json()["data"]["contentlist"][numle-1]["comment"]#查到的最后一个元素是否相同
    return res


@de.prt
@de.posturl("获取评论列表",2)
def test_01_getcomment_success_type2(res,url,head,body):
    sqlcount = "SELECT count(*) FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(body["ctype"],body["fid"],10*(int(body["pagenum"])-1))
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
            DESC LIMIT {},10;".format(body["ctype"],body["fid"],10*(int(body["pagenum"])-1))
    numle = num%10#第一页第几个，如果总数大于10，取余数，总数小于10，取本身
    assert num == 0 or db.query(sql)[numle-1][0] == res.json()["data"]["contentlist"][numle-1]["comment"] #查到的最后一个元素是否相同
    return res


@de.prt
@de.posturl("获取评论列表",3)
def test_01_getcomment_success_type3(res,url,head,body):
    #判断数据量是否相等
    sqlcount = "SELECT count(*) FROM t_user_comments c \
           join t_user u on c.uid=u.id \
            WHERE ctype = {} \
            AND fid = {} \
            AND c.STATUS = 0 \
            ORDER BY c.updatetime \
            DESC LIMIT {},10;".format(body["ctype"],body["fid"],10*(int(body["pagenum"])-1))
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
            DESC LIMIT {},10;".format(body["ctype"],body["fid"],10*(int(body["pagenum"])-1))
    numle = num%10#第一页第几个，如果总数大于10，取余数，总数小于10，取本身
    assert num == 0 or db.query(sql)[numle-1][0] == res.json()["data"]["contentlist"][numle-1]["comment"] #查到的最后一个元素是否相同
    return res


@de.prt
@de.posturl("获取评论列表",4)
def test_01_getcomment_fail_typenotexist(res,url,head,body):
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 401#结果码
    assert res.json()["msg"] == "ctypectype不在范围内，0教程1提问2灵感3心得体会"#提示信息
    return res


@de.prt
@de.posturl("获取评论列表",5)
def test_01_getcomment_fail_fidnotint(res,url,head,body):
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 401#结果码
    assert res.json()["msg"] == "fid【{}】应该是正整数才行！".format(body["fid"])#提示信息
    return res


@de.prt
@de.posturl("获取评论列表",6)
def test_01_getcomment_fail_fidnull(res,url,head,body):
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "fid不能为空"#提示信息
    return res


@de.prt
@de.posturl("获取评论列表",7)
def test_01_getcomment_fail_ctypenull(res,url,head,body):
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "ctypectype不在范围内，0教程1提问2灵感3心得体会"#提示信息
    return res


@de.prt
@de.posturl("获取评论列表",8)
def test_01_getcomment_fail_pagenull(res,url,head,body):
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "pagenum不能为空"#提示信息
    return res     


@de.prt
@de.posturl("获取评论列表",9)
def test_01_getcomment_fail_pagetoobig(res,url,head,body):
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "页码超出范围"#提示信息
    return res


@de.prt
@de.posturl("获取评论列表",10)
def test_01_getcomment_fail_pagexiaoshu(res,url,head,body):
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "pagenum【{}】应该是正整数才行！".format(body["pagenum"])#提示信息
    return res


@de.prt
@de.posturl("获取评论列表",11)
def test_01_getcomment_fail_pagechar(res,url,head,body):
    assert res.json()["status"] == 401#结果码
    assert res.status_code == 200#状态码
    assert res.json()["msg"] == "pagenum【{}】应该是正整数才行！".format(body["pagenum"])#提示信息
    return res