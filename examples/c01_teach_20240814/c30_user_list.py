arr = [
    {"name": "张三", "age": 13},
    {"name": "李四", "age": 23},
    {"name": "王五", "age": 33},
]
target_name = "李四"

index = 0
for v in arr:
    print(v)
    if v["name"] == target_name:
        print("找到了索引：", index)
        break
    index += 1

print(arr[index])
