'''获取token'''

import pymysql # 要想用pymysql，就必须要导入它
import os,sys
import case.登录注册相关.test_02_login as te
sys.path.append(os.getcwd())

def getoken():
    res1 = te.test_01_login_success(1,1,1,1)#这里两个参数取什么都无所谓
    token = res1.json()["data"]["token"]
    return token   

if __name__ == "__main__":
    a = query("select * from t_user where id = 1111")
    print(a)