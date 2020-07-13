def add(n):
    num = 1
    sum = 0
    while num <= n:
        sum = sum + num
        num = num + 1
    return sum

n = 10
while n <= 100:
    print("add ", n, " => ", add(n))
    n = n + 10
