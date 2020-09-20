import os,sys
sys.path.append(os.getcwd())
import pytest
import requests
import utils.decorate as de
import utils.exceltools as extool
import utils.dbtools as db
@de.outer
def test_01_getmblist_success():
    e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", "获取密保问题列表")
    url = e_data[0][2]
    head = eval(e_data[0][5])
    res = requests.get(url=url,headers=head)#head中规定使用json，因此用json而不是data
    assert res.json()["status"] == 200#状态码
    assert res.status_code == 200#结果码
    return res