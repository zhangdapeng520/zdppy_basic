arr = [1, 2, 3, 33, 44, 55]
target = 33

index = 0
for v in arr:
    print(v)
    if v == target:
        print("找到了索引：", index)
        break
    index += 1

print(arr[index])
