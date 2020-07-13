class Person():
    name = ""
    def __init__(self):
        print("Person created")

class Employee(Person):
    job_title = ""
    def __init__(self):
        print("Employee created")

class Customer(Person):
    email = ""
    def __init__(self):
        print("Customer created")

john_smith = Person()
jane_employee = Employee()
bob_customer = Customer()
