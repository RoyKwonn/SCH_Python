def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ') # end=' '는 줄바꿈을 없애기 위함이다.
        a, b = b, a + b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    fib(50)
