import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
import utils.dbtools as db
import utils.decorate as de
import utils.exceltools as extool

@de.outer
def test_01_showversion_success():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取版本")
    url = e_data[0][2]
    head = eval(e_data[0][5])
    res = requests.get(url=url,headers=head)
    assert res.status_code == 200#状态码
    assert res.json()["status"] == 200#结果码
    return res