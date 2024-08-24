# 假设我们现在想要根据输入月份，判断是哪个季节，怎么做呀？

month = int(input("请输入月份："))

if month in [12, 1, 2]:
    print("冬天")
elif month in [3, 4, 5]:
    print("春天")
elif month in [6, 7, 8]:
    print("夏天")
elif month in [9, 10, 11]:
    print("秋天")
else:
    print("错误的月份：", month)
