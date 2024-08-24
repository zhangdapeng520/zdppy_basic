num = 11

for i in range(2,num):
    if num % i == 0:
        print("不是质数")
        break
else:
    print("是质数")