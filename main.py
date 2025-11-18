"""Birthday problem"""

date = int(input("Enter a date: "))
mon = int(input("Enter a month "))

year = 2024

if(date == 28 and mon == 9):
    print("Today is",date,"/",mon,"/",year ,"and it's your bithday")
    print("Happy Birthday")

else:
    """print("It is not your birthday")"""
    
"""Grading problem"""

marks = int(input("Enter the marks: "))

if(marks >= 90):
    print("O Grade")
elif(marks >= 80 and marks <= 90):
    print("A+ ")
elif(marks >= 70 and marks <= 80):
    print("A")
elif(marks >= 60 and marks <= 70):
    print("B")
elif(marks >= 50 and marks <= 60):
    print("C")
elif(marks >= 40 and marks <= 50):
    print("D")
else:
    print("Sorry you got less marks")
    
"""single line condition statement"""

food = input("Enter your dish: ")

eat = "Yes" if food == "Samosa" or food == "momos" else "no"
print(eat)

"""clever if condtn"""

age = int(input("age: "))
vote = ("Yes", "no") [age <= 18]

""" Operators """

a = 50
b = 20

print(a!=b)

number = float(input("Enter the number in decimal: "))
number = number * number

print(number)

""" Type conversion """

a = 12
b = 12.80
# auto conversion of int into float value 
sum = a + b
# print(sum)

""" Type casting """

# str = "9"
num = 2230
# print(str + num)#Error 

str = int("9")
print(str + num) 