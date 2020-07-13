def sum(n):
    if (n == 1):
        return 1
    else:
        return sum(n-1) + n


print("add(10) => ", sum(10))
print("add(100) => ", sum(100))
