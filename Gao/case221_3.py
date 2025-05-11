#decorator实践，日志追踪
from functools import wraps

def long_ars_and_response(log_level):#装饰器工厂
    def actual_decorator(func):#装饰器
        @wraps(func)#functools模块的一个装饰器，用于保留被装饰函数的元信息（函数名、文档字符串）
        def log_func(*args, **kwargs):#包装函数
            print("%s: begin %s(%s, %s)" % (log_level, func.__name__, args, kwargs))
            res = func(*args, **kwargs)#调用被封装的函数，调用的结果赋值给res
            print("%s: end %s(%s, %s)" % (log_level, func.__name__, args, kwargs))
            return res
        return log_func#将包装函数返回，替代原函数func
    return actual_decorator#装饰器的实际实现，不返回的话，装饰器无法接受被装饰的函数作为参数

@long_ars_and_response("debug")
def process():
    print("processing...")
process()