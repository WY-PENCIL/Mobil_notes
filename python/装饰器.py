#装饰器
# 定义：装饰器本质上是一个函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
# 装饰器的作用就是为已经存在的函数添加额外的功能。

#装饰器需要满足以下两点
# 1. 不修改源程序或函数的代码
# 2. 不修改源程序或函数的调用方法

# 装饰器的原则就不不入侵源代码或原函数，只做增强功能，因为有的核心代码不是你想改就能改的

# 装饰器语法糖
# @装饰器名
# def 函数名():
#     ...

# 装饰器执行顺序
# 1. 先执行装饰器函数
# 2. 再执行被装饰的函数
# 3. 最后返回被装饰的函数

#代码编写中如果发现很多行为需要共同扩展一个相同的能力，那么就可以编写一个装饰器来扩展这个能力，没有必要每个函数都去扩展这个能力。

# 1. 装饰器的基本使用
# def outer(func):
#     def inner():
#         print("这是装饰器")
#         func()
#     return inner

# @outer
# def fun():
#     print("这是被装饰的函数")

# fun()

# 2. 装饰器带参数
# def outer(arg):
#     def inner(func):
#         def wrapper():
#             print("这是装饰器")
#             func()
#         return wrapper
#     return inner

# @outer("hello")
# def fun():
#     print("这是被装饰的函数")

# fun()

# 3. 装饰器装饰多个函数
# def outer(func):
#     def inner():
#         print("这是装饰器")

#         func()
#     return inner

# @outer
# def fun1():
#     print("这是被装饰的函数1")

# @outer
# def fun2():
#     print("这是被装饰的函数2")

# fun1()
# fun2()


# 标准版的装饰器
def wrapper(func):
    def inner(*args,**keywargs):
        # 执行函数之前的操作
        print("执行函数之前的操作")
        ret = func(*args,**keywargs)
        # 执行函数之后的操作
        print("执行函数之后的操作")
        return ret
    return inner

@ wrapper
def fun1 (a,b):
    print ("这是被装饰的函数1",a,b)

fun1(1,2)# 使用了装饰器的普通函数调用