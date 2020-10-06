import os,sys
sys.path.append(os.getcwd())
import utils.exceltools as extool
import requests
'''装饰器，一个bug，断言失败时，无法打印'''
def prt(fun):
    '''打印装饰器，用于打印每个请求的响应'''
    def wrapper(*args, **kwargs):      
        sub = fun(*args, **kwargs)
        print(sub.text)
        return sub#此必不可少，否则两次装饰后，函数没有返回值
    return wrapper

def geturl(sheet_name,row_number):
    '''获取请求装饰器，用于获取请求，输入参数为表格行数及表格的名称'''
    def wrapper1(fun):
        def wrapper2(*args, **kwargs):
            e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", sheet_name)
            url = e_data[row_number][2]
            head = eval(e_data[row_number][5])
            res = requests.get(url=url,headers=head)
            sub = fun(res,url,head)
            return sub
        return wrapper2
    return wrapper1

def posturl(sheet_name,row_number):
    '''post请求装饰器，用于获取请求，输入参数为表格行数及表格的名称'''
    def wrapper1(fun):
        def wrapper2(*args, **kwargs):
            e_data = extool.read_excel("data/测谈网接口测试用例.xlsx", sheet_name)
            url = e_data[row_number][2]
            head = eval(e_data[row_number][5])
            body = eval(e_data[row_number][4])
            res = requests.post(url=url,headers=head,json=body)#head中规定使用json，因此用json而不是data
            sub = fun(res,url,head,body)
            return sub
        return wrapper2
    return wrapper1


