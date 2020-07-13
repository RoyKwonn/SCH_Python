# 컴퓨터공하과 20184646 권석환 


class Work_Start(): # 근무 시작 클래스 
    name = ""
    def __init__(self, nam): ## 생성자 메소드 이름을 입력하면 출근에 관한 내용을 택스트로 저장
        self.name = nam
    def save(self):
        file = open("diligence.txt", "a") # 파일에 append 이어 붙이기 한다.
        file.write("%07s%07s\n" % (self.name, "출근")) # 7칸씩 뛰어 이름과 출근을 저장한다.
        file.close()

class Work_End(Work_Start): # 근무 종료 클래스 Work_Start를 상속받는다.
    def __init__(self, nam):
        self.name = nam
    def save(self): # Work_Start의 save()메소드를 오버라이딩한다.
        file = open("diligence.txt", "a")
        file.write("%07s%07s\n" % (self.name, "퇴근")) # 택스트 파일에 이름과 퇴근을 이어붙이기
        file.close()

employee = ["홍인식", "이상정", "하상호", "천인국"] # 리스트로 교수님 이름 만들기
running = True

print("교수님들 문 앞에 붙어있는 현황표 (부재중, 재실, 수업중)을 비슷하게 구현해봤습니다.")

while running:
    option = 1
    for choice in employee:
        print(str(option) + ". " + choice) # 각각 번호에 맞게 교수님들 이름 출력
        option += 1
    print(str(option) + ". 입력 종료 후 최종 교수님들 상태보기")
    choice = int(input("Choose an option : "))
    if choice == option : # 만약 맨 마지막 option을 입력한다면. 반복문 종료
        running = False
    else:
        work = input("출근은 s, 퇴근은 e : ")
        if work == "s":
            working = Work_Start(employee[choice-1]) # 입력한 교수님에 대한 내용을 저장한다.
            working.save()
        elif work == "e":
            working = Work_End(employee[choice-1]) # 입력한 교수님에 대한 내용을 저장한다.
            working.save()

f = open("diligence.txt") # 파일을 읽어오기 위하여 선언

names = {} # Hash로 선언해준다. 두가지 값을 연결하기 위함이다.

for line in f: # 파일을 한줄 씩 읽어온다.
    (name, state) = line.split()
    names[name] = state # key를 각각의 이름으로 설정하여 이름에 따른 최종 값을 등록하도록 만든다.

f.close() # 파일을 읽으면 꼭 close()를 선언해준다.

print("현재 교수님들 상태")
    
for each_name in sorted(names.keys()):
    print( each_name +" " + names[each_name]) # 해쉬를 이용하여 최종값을 출력해준다.
