import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.dbtools as db
import utils.decorate as de
import utils.exceltools as extool

@de.geturl("获取版本",0)
@de.prt
def test_01_showversion_success(res,url,head):
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 200#结果码
    return res