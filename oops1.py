""" Introduction to OOP """
# class and objects

# class Student:
#     name = input("Enter the name: ")
#     roll_no = int(input("Enter roll no: "))
#     branch = "CSE"

# s1 = Student() # instance for class Student

# print(s1.name)
# print(s1.roll_no)
# print(s1.branch)

# class Toyota:
#     model = "Innova"
#     manufacturin = "India"
    
# car = Toyota()
# print(car.model)
# print(car.manufacturin)

""" Init func """

# class Student:
    
#     #default constructor
#     def __init__(self):
#         pass
#     #parameterized constructor
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("new student")

# s1 = Student("Daksh",99)
# print(s1.display, s1.marks)

# s2 = Student("Harsh",90)
# print(s2.display, s2.marks)

""" Class attr and object attr """

# class Student:
#     college = "LPU" # class attribute can be accessed by any object
#     name =  "anonymous"
#     #default constructor
#     def __init__(self):
#         pass
#     #parameterized constructor
#     def __init__(self,name,marks):
#         self.display = name # obj attr > class attr
#         self.marks = marks
#         print("new student")

# s1 = Student("Daksh",99)
# print(s1.display, s1.marks, s1.college)

# s2 = Student("Harsh",90)
# print(s2.display, s2.marks, s2.college)

""" Methords """

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     # methord 
#     def  sayHello(self):
#         print("Hello, welcome back", self.name)
    
#     def getmarks(self):
#         print(self.marks)
    
# # instance for class student
# s1 = Student("Harsh", 19)
# s1.sayHello() # methord func calling
# s1.getmarks() # methord func calling

""" """## Question

# class student:
#     # parameter constructor
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
    
#     def average(self):
#         print((self.marks1 + self.marks2 + self.marks3) / 3)

# stu = student("Ajay", 18,45,21)
# print(stu.name,stu.marks1,stu.marks2,stu.marks3)
# stu.average()

""" @staticmethords """

# class student:
#     # parameter constructor
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
# ##  staticmethord
#     @staticmethod    
#     def hello():
#         print("Hello")
    
#     def average(self):
#         print((self.marks1 + self.marks2 + self.marks3) / 3)

# stu = student("Ajay", 18,45,21)
# print(stu.name,stu.marks1,stu.marks2,stu.marks3)
# stu.average()
# stu.hello()

""" Abstraction """

# class Car:
#     def __init__(self):
#         self.acclrate = False
#         self.engine = False
#         self.clutch = False
        
#     def StartCar(self):
#         self.engine = True
#         self.clutch = True
#         self.acclrate = True
#         print("Car started ..")
        
# car1 = Car()
# car1.StartCar()

""" Questions """

class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
        
acc1 = Account(12526500761.89, "1a2FJxxxx67")
print(acc1.balance)
print(acc1.account_no)

class Account:
    
    def __init_subclass__(self):
        pass
    
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
        
    #debit methord
    def debit(self, amount):
        self.balance -= amount
        print(amount,"Rs.has been debited sucessfully")
        print("Updated balance:",self.getBalance())

    #credit methord
    def credit(self, addmoney):
        self.balance += addmoney
        print(addmoney,"Rs.has been credited sucessfully")
        print("Updated balance:",self.getBalance())
        
    def getBalance(self):
        return self.balance
        
acc1 = Account(12526500761.89, "1a2FJxxxx67")
# print(acc1.balance)
# print(acc1.account_no)

acc1.debit(9127)
acc1.debit(123352)
acc1.credit(978602)
acc1.getBalance()
