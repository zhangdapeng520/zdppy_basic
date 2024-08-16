# 定义字典
d = {}

# 追加数据
d["name"] = "张三"
d["age"] = 23
print(d)

# 用户列表：[{name:xxx,age:xxx},{}]
# 修改，当这个key已经存在，就会发生修改
d["name"] = "张三333"
print(d)

# 根据key查询
print(d["name"])

# 根据key删除
del d["age"]
print(d)
