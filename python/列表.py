a=[]
b=[1,2,3,4]
a.append("initData")
a.extend(b)

a.insert(len(a),'add')
a.insert(5,"wang") #在指定位置插入元素，这个方法不会删除列表里面任何一个元素，只是把元素插入到指定位置
a.remove("add") #删除第一个值为add的元素,
#a.pop() #删除指定位置的元素,如果传值则删除指定位置元素，不传值则删除最后一个元素
print(f"寻找指定位置元素：{a.index(3,0)}")

print(a)
if a.index(3,4):
    print("3")
elif a:
    print("1")
else:
    print("0")