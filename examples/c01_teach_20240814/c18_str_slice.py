s1 = "abcde"

# 默认值
print(s1[:])  # abcde

# -1
print(s1[:-1])  # abcd 足以证明，结束索引默认值不是-1

# 数组长度
print(s1[:len(s1)])  # abcde 所以，结束索引的默认值极可能是数组的长度
