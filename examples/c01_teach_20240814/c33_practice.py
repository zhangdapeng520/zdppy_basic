arr = [
    {"name": "张三", "age": 13},
    {"name": "李四", "age": 23},
    {"name": "王五", "age": 33},
]
target_name = "李四"

for i in range(len(arr)):
    if arr[i]["name"] == target_name:
        print("找到了索引：", i, arr[i]["name"], arr[i])
        break
