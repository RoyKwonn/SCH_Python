def add(n):
    num = 1
    sum = 0
    while num <= n:
        sum = sum + num
        num = num + 1
    return sum

print("add(10) => ")
print(add(10))

print("add(100) => ", add(100))
