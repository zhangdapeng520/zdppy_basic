def is_prime(num):
    """判断是否为质数"""
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


count = 0
for i in range(1, 101):
    if is_prime(i):
        count += i
print(count)
