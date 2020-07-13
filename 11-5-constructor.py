class Dog():
    name = "Rover"
    def __init__(self, name): # 생성자
        print(self.name)
        print(name)
        self.name = name

my_dog = Dog("sport")

print(my_dog.name)
