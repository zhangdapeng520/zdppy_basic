# 左边空格
s1 = "             abc"
print("===", s1, "===")
print("===", s1.lstrip(), "===")

# 右边空格
s2 = "bbc                    "
print("===", s2, "===")
print("===", s2.rstrip(), "===")

# 左右两边空格
s3 = "           ccc                 "
print("===", s3, "===")
print("===", s3.strip(), "===")
