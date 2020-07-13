# 누적 짝수 덧셈 프로그램
# 초기값
number = 2
sum = 0

n = input("N : ")
end = int(n)

while number <= end:
    sum = sum + number
    print(number, sum)
    number = number + 2

print("누적 합 : ", sum)
