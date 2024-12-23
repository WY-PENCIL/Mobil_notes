#闭包
#定义：在嵌套函数的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们就把使用了外部函数的内部函数称为闭包

#闭包的条件：
#1. 函数嵌套
#2. 内部函数要使用外部函数的局部变量
#3. 外层函数的返回值是内层函数的函数名


#闭包的作用：保存外部函数的变量，延长外部函数的变量的生命周期

#闭包的缺点：由于闭包引用了外部函数的变量，则外部函数的变量没有及时释放，消耗内存

#闭包的写法
def outer():
    x = 10
    def inner():
        print(x)
    return inner
#闭包的调用
f = outer() # 函数名里面保存的是函数所在内存中的地址，返回的是一个引用地址，所以要执行函数就需要在这个地址引用地址后面加括号
f() # 所以这里需要加上括号，才会去执行函数

# 引用，你就可以理解为内存地址

a = 2
print(id(a)) # a只是引用了值2的内存地址
print(id(2)) # 2是值，值在内存中的地址

# 所以函数加了小括号，就会去执行这个引用的内存函数，不加上小括号，就只是引用了函数的内存地址

# 闭包每次开启内函数都在使用同一份闭包变量，所以闭包变量是共享的
# 闭包的变量是共享的，所以闭包的变量不能是可变类型

def outer(m):
    def inner(n):
        return m+n
    return inner
f = outer(10) # 先构建为一个闭包结构，传入一个外部函数的局部变量，用于每次开启闭包的共享变量

print(f(10)) #开启一个闭包，每执行一次内部函数就叫开启一此闭包

print(f(20)) # 开启第二次闭包，传入的参数是20，所以结果为30 

# 上面一共开启了两次闭包，产生的对象是不一样的，但是他们都共享着同一份闭包变量，所以闭包变量是共享的