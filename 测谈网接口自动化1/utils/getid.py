'''获取各种id'''

import pymysql # 要想用pymysql，就必须要导入它
import os,sys
import case.其他post相关.test_03_quenew as gid
import case.其他post相关.test_06_insnew as giid
import case.其他post相关.test_09_artinew as gaid
sys.path.append(os.getcwd())

def getqid():
    res1 = gid.test_01_quenew_success(1,1,1,1)#这里两个参数取什么都无所谓
    qid = res1.json()["data"]["questionid"]
    return qid

def getiid():
    res1 = giid.test_01_insnew_success(1,1,1,1)#这里两个参数取什么都无所谓
    iid = res1.json()["data"]["inspirerid"]
    return iid

def getaid():
    res1 = gaid.test_01_artinew_success(1,1,1,1)#这里两个参数取什么都无所谓
    aid = res1.json()["data"]["articleid"]
    return aid


if __name__ == "__main__":
    a = query("select * from t_user where id = 1111")
    print(a)