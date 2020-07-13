# 리스트의 메서드를 사용하여 단어의 개수를 리턴하는 함수
def wCount(word):
    wlist = []
    for wd in text.split():     # text 변수의 내용을 공백문자로 분리한 리스트
        wlist.append(wd)
    cnt = wlist.count(word) # 리스트의 count 메서드 적용
    return cnt

f = open("imagine.txt")
text = f.read() # 파일 읽기, 전역변수(global variable)

w= "Imagine"
n = wCount(w)   # 함수 호출
print(w + ":" + str(n)) # 단어 개수 출력

## 복수의 단어 카운트
wlist = ["Imagine", "people", "dreamer"]
s = {}

# 단어가 키, 개 수가 값이 되도록 해시에 저장
for wd in wlist:
    n = wCount(wd) # 함수호출 
    s[wd] = n

print(s)
