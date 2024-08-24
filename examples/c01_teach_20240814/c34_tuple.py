# 空元组
t = tuple()
print(t, type(t))

# 有元素的元组
t2 = (1, 2, 3)
print(t2, type(t2))

# 直接遍历元组
for v in t2:
    print(v)

# 通过索引访问元组
for i in range(len(t2)):
    print(t2[i])
