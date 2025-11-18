""" Welcome to part 2 """
## part 2 of oops 

""" del keyword """
 
# class Student:
#     def __init__(self,name):
#         self.name = name
        
# s1 = Student("Harsh")
# print(s1.name)
# del s1 ## use to delete the attr or an entire object
# print(s1.name)

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass ## private attr by using __ in variable name
        
#     def reset_pass(self):
#         print(self.__acc_pass)
        
# acc1 = Account("12315634", "abcD@12")
# print(acc1.acc_no)
# # print(acc1.__acc_pass) # error
# acc1.reset_pass()

""" Inheritance """ ## single inheritance

# class Car: # parent class
#     @staticmethod
#     def start():
#         print("Car start..")
        
#     @staticmethod
#     def stop():
#         print("Car stop..")
    
# class Toyota(Car):# child class
#     def __init__(self, name, model):
#         self.name = name 
#         self.model = model
        
# Car1 = Toyota("land cruiser", 2016)
# car2 = Toyota("supra MK4", 1999)

# Car1.start()
# print(Car1.name, Car1.model)
# car2.start()
# print(car2.name, car2.model)

""" types """
## multiple inheritence ##

# class Car: # parent class
#     @staticmethod
#     def start():
#         print("Car start..")
        
#     @staticmethod
#     def stop():
#         print("Car stop..")
    
# class Toyota(Car):# child class
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
# class Fortuner(Toyota): # child class
#     def __init__(self, type):
#         self.type = type
        
# #instance for class
# car1 = Fortuner("deisel")
# car1.start()


## multi level inheritence ##

# class Father:
#     def __init__(self, name, age, job):
#         self.name = name
#         self.age = age
#         self.job = job
        
# class Mother:
#     def __init__(self, name, age, job):
#         self.name = name
#         self.age = age
#         self.job = job

# class child(Father, Mother):
#     def __init__(self,name,age,job,gender):
#         Father.__init__(self,name,age,job)
#         self.gender = gender

# dad = Father("Ajay", 45, "Sales")
# mom = Mother("Nirmal", 45, "housewife")
# c1 = child("Daksh",15,"Student","Male")

# print(dad.name,dad.age,dad.job)
# print(mom.name,mom.age,mom.job)
# print(c1.name,c1.age,c1.job,c1.gender)

""" Super methord """

# class Car: # parent class
#     def __init__(self,type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         print("Car start..")
        
#     @staticmethod
#     def stop():
#         print("Car stop..")
    
# class Toyota(Car):# child class
#     def __init__(self, brand,type):
#         self.brand = brand
#         # self.model = model
#         super().__init__(type)
        
        
# #instance for class
# car1 = Toyota("Safari","deisel")
# print(car1.type)
# print(car1.brand)

""" class methord """

# class Person:
#     name = "anonymous"
    
#     @classmethod #decorator
#     def changeName(cls, name):
#         cls.name = name 
       
# p1 = Person()
# p1.changeName("Harsh")
# print(p1.name)
# print(Person.name)

""" Property decorator """

# class Student:
#     def __init__(self,physics,chem,math):
#         self.physics = physics
#         self.chem = chem
#         self.math = math
        
#     @property
#     def percentage(self):
#         return str((self.physics+self.chem+self.math) / 3) + "%"
        
# s1 = Student(98, 97, 99)
# print(s1.percentage)
# s1.physics = 89 # value gets updated 
# print(s1.percentage)

""" Polymorphism """
## operator overloading 

# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
        
#     def showno(self):
#         print(self.real,"i +",self.img,"j")
        
#     def __add__(num1, num2):
#         newreal = num1.real + num2.real
#         newimg = num1.img + num2.img
#         return Complex(newreal, newimg)
    
#     def __sub__(num1, num2):
#         newreal = num1.real - num2.real
#         newimg = num1.img - num2.img
#         return Complex(newreal, newimg)
        
# no1 = int(input("Enter no: "))
# no2 = int(input("Enter no: "))
# no3 = int(input("Enter no: "))
# no4 = int(input("Enter no: "))

# num1 = Complex(no1, no2)
# num1.showno()

# num2 = Complex(no3, no4)
# num2.showno()

# num3 = num1 + num2
# num4 = num1 - num2
# print("The sum of complex numbers:-")
# num3.showno()
# print("The difference is ")
# num4.showno()

""" Question """

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     def Area(self):
#         area = 3.14 * self.radius * self.radius
#         print(f"Area: {area:.2f}")
        
#     def perimeter(self):
#         permtr = 2 * 3.14 * self.radius
#         print(f"Perimeter: {permtr:.2f}")

# rad = int(input("Enter the radius: "))      
# c1 = Circle(rad)
# c1.Area()
# c1.perimeter()

# class Employee:
#     def __init__(self,role,department,salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
        
#     def showDetails(self):
#         print(self.role)
#         print(self.department)
#         print(self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age,role,department, salary):
#         self.name = name
#         self.age = age
#         super().__init__(role, department, salary)
#         # super().__init__(role2, department2, salary2)
        
#     def Show(self):
#         print(self.name)
#         print(self.age)
#         self.showDetails()

# name1 = input("Enter your name: ")
# age1 = int(input("Enter your age: "))
# role1 = input("Enter the role: ")
# department1 = input("Enter the department: ")
# salary1 = float(input("Enter your salary: "))

# e1 = Engineer(name1, age1, role1, department1, salary1)
# e1.Show()

# name2 = input("Enter your name: ")
# age2 = int(input("Enter the age: "))
# role2 = input("Enter the role: ")
# department2 = input("Enter the department: ")
# salary2 = float(input("Enter your salary: "))

# e2 = Engineer(name2, age2, role2, department2, salary2)
# e2.Show()

# class Complex:
#     def __init__(self, order, price):
#         self.order = order
#         self.price = price
        
#     def __gt__(c1, c2):
#         return c1.price > c2.price
            
# c1 = Complex("Burger", 40)
# c2 = Complex("Pizza", 110)

# print(c1 > c2) # to check c1 is less than c2 

""" Ques asked in python exam """

class Bookstore:
    def __init__(self,title,copies):
        self.__title = title
        self.__copies = copies
        
    def get_title(self):
        return self.__title
    
    def get_copies(self):
        return self.__copies
    
    def sell_copies(self,copies_in_sell):
        self.copies_in_sell = copies_in_sell
        
        if self.__copies >= self.copies_in_sell and self.copies_in_sell >= 1:
            return self.__copies - self.copies_in_sell
            # print(self.__copies)
        else:
            return "Invalid output"

t1 = input("Enter the title: ")
cpy = int(input("Enter the no of copies: "))
sell_cpy = int(input("Enter the no fo books sold: "))

book = Bookstore(t1, cpy)
print(book.get_title())
print(book.get_copies())
result = book.sell_copies(sell_cpy)
print(result)