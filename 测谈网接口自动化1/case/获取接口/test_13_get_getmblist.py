import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.decorate as de
import utils.exceltools as extool
import utils.dbtools as db
import utils.decorate as de

@de.geturl("获取密保问题列表",0)
@de.prt
def test_01_getmblist_success(res,url,head):
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res