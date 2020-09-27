import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.geturl("获取首页轮播图",0)
@de.prt
def test_03_getpicture(res,url,head):
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select * from t_title_img where status = 0 "
    assert len(db.query(sql)) == len(res.json()["data"])#判断数据库中轮播图数量是否相等
    return res