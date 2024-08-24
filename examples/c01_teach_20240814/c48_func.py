def get_season(month):
    """获取"""
    if month in [12, 1, 2]:
        return "冬天"
    elif month in [3, 4, 5]:
        return "春天"
    elif month in [6, 7, 8]:
        return "夏天"
    elif month in [9, 10, 11]:
        return "秋天"
    else:
        return "错误的月份"


while True:
    v = input("请输入月份：")
    if v == "exit":
        break
    print(get_season(int(v)))
