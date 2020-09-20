import os,sys
sys.path.append(os.getcwd())
def outer(fun):#装饰器，用于打印每个请求的响应
    def inner():      
        fun()
        print(fun().text)
    return inner