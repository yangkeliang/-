import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import utils.dbtools as db
def test_03_getpicture():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取首页轮播图")
    url = e_data[0][2]
    head = eval(e_data[0][5])
    res = requests.get(url=url,headers=head)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select * from t_title_img where status = 0 "
    assert len(db.query(sql)) == len(res.json()["data"])#判断数据库中轮播图数量是否相等