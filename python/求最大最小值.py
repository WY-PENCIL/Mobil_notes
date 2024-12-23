
from functools import reduce
obj = [{'name':"张三","age":10},{'name':"李四","age":20},{'name':"王五","age":30}]

# # 求最大年龄
max_age = reduce(lambda x,y: x if x['age']>y['age'] else y,obj)
print(f"最大年龄是：{max_age['name']}他的年龄是：{max_age['age']}")

# a = "123432"
# print(int(a))