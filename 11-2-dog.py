class Dog():
    # 속성
    age = 0
    name = ""
    weight = 0

    # 메서드
    def bark(self):
        print("%s -> 멍멍" % self.name)

myDog = Dog() # 인스턴스 생성
myDog.name = "Merry"
myDog.weight = 20
myDog.age = 3
myDog.bark() # 메서드 호출

yourDog = Dog()
yourDog.name = "Happy"
yourDog.weight = 30
yourDog.age = 5
yourDog.bark()
