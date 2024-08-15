name1 = "   AbcD   "
print(name1)

name2 = input("请输入验证码：")

name1 = name1.strip()
name2 = name2.strip()

name1 = name1.upper()
name2 = name2.upper()

if name1 == name2:
    print("输入正确")

else:
    print("输入错误")
