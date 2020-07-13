text = """
    Sonnchunhyang Unibersity
    Dept. of Computer Science and Engineering
"""

# 파일 쓰기
f = open("test.txt", "w")
f.write(text.lower())
f.close()

# 파일 읽기
f = open("test.txt", "r") # = open("test.txt")라고만 써도 됨
lines = f.read()
print(lines)
f.close() #교수님께서 빠트린 것
