# 用户列表
users = []

# 增加用户：id，name，age => {id:1, name:张三, age: 23}
users.append({
    "id": 1,
    "name": "张三",
    "age": 23,
})
users.append({
    "id": 2,
    "name": "李四",
    "age": 24,
})
print(users)

# 张三 改为 张三丰
users[0]["name"] = "张三丰"
print(users)

# 删除李四
del users[1]
print(users)
