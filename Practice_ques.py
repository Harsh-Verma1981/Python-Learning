## ques 1 by variables

# a = 12
# b = 21

# a,b = b,a
# print(a)
# print(b)

## ques 2

# age = int(input("Enter your age: "))
# ageConversion = age * 12

# print("Total months in", age, "years:", ageConversion,"months")

## ques 3

# temp = int(input("Enter the temp: "))
# farn = (9/5 * temp) + 32
# print(f"{farn:.2f}")

## ques 1 from operators

# val1 = int(input("Enter value 1: "))
# val2 = int(input("Enter value 2: "))

# print("Addition:",val1 + val2)
# print("Subtraction:", val1 - val2)
# print("Multiplication:", val1 * val2)
# print("Division:", val1 / val2)

## ques 2 

# a = 4
# b = 2
# print(a%b)

## ques 3

# x = 42
# y = 24
# if(x == y):
#     print("Equal")
# elif(x > y):
#     print("X is greatest")
# else:
#     print("X is smallest")

## ques 1 from if else

# x = 4
# if(x%2==0):
#     print("Even")
# else:
#     print("Odd!")

## ques 2

# year = 2024
# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

## ques 3

# age = 18
# if(age >= 18 ):
#     print("You can vote")
# else:
#     print("You can't vote")

## loops ques 1

# for i in range(2, 50+2, 2):
#     print(i)

## ques 2

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n - 1)
    
# n = int(input("Enter the no: "))
# fact(n) # recursive func call
# print(fact(n))

## ques 3

# def Addtn(n):
#     if(n == 0):
#         return 0
#     else:
#         return n + Addtn(n - 1)
    
# n = int(input("Enter the no: "))
# Addtn(n) # recursive func call
# print(Addtn(n))

## List ques 1

# def find_largest(numbers):
#     # Function to find the largest number in the list
#     numbers.sort()
#     return numbers[-1]
#     pass  # Replace this with your code

# def find_smallest(numbers):
#     # Function to find the smallest number in the list
#     numbers.sort()
#     return numbers[0]
#     pass  # Replace this with your code

# def main():
#     # Sample list of numbers
#     numbers = [34, 67, 23, 89, 12, 56]

#     # Call the functions and store the results
#     largest = find_largest(numbers)
#     smallest = find_smallest(numbers)

#     # Print the results
#     print("Largest number:", largest)
#     print("Smallest number:", smallest)

# # Run the main function
# if __name__ == "__main__":
#     main()

## ques 2    

# def findeven(setofnums):
#     seteven = []# empty list to store even values
#     for num in setofnums:
#         if num % 2 == 0:
#             seteven.append(num)
            
#     return seteven


# def main():
#     setofnums = []
#     n = int(input("Enter the size: "))
#     for i in range(n):
#         no = int(input("Enter the number: "))
#         setofnums.append(no)
        
#     even = findeven(setofnums)
#     print(even)
        
# if __name__ == "__main__":
#     main()

## ques 3 

# def Count(list1):
#     key = int(input("Enter key to find: "))
#     for num in list1:
#         list1.count(key)

#     return list1.count(key)

# def main():
#     list1 = []
#     n = int(input("Enter size: "))
#     for i in range(n):
#         no = int(input("Enter number: "))
#         list1.append(no)
        
#     c1 = Count(list1)
#     print(c1)

# if __name__ == "__main__":
#     main()
        
## strings Ques 1

# str = input("Enter the string: ")

# count = 0
# vowels = ['a', 'e', 'i', 'o', 'u']

# for char in str:
#     if (char.lower() in  vowels):
#         count += 1
        
# print(count)

## ques 2    

# def is_palindrome(str):
#     # Convert the string to lowercase to make it case-insensitive
#     str = str.lower()
    
#     # Check if the string is equal to its reverse
#     return str == str[::-1]

# def main():
#     # Get user input for the string
#     str_input = input("Enter the string: ")
    
#     # Check if the string is a palindrome and print the result
#     if is_palindrome(str_input):
#         print("The string is a palindrome.")
#     else:
#         print("The string is not a palindrome.")

# # Run the main function
# if __name__ == "__main__":
#     main() # call 

## ques 3

# def get_words(sentence):
#     # divide the string into words
#     words = sentence.split()
    
#     for word in words:
#         print(word) # loop to get each word

# def main():
#     # input from user 
#     sentence = input("Enter the sentence: ")
#     # calling get_word func
#     get_words(sentence)
    
# if __name__ == "__main__":
#     main()

""" func ques 1"""

# def sumoftwo(a, b):
#     print("Sum:",a + b)
#     print("Average:",(a + b)/2)
    
# no1 = 24
# no2 = 9

# sumoftwo(no1, no2)

## ques 2

# def prime(n):
#     squreroot = n ** 0.5
#     if n <= 1:
#         print(n, "is not a prime no")
#         return
    
#     for i in range(2, int(squreroot)+1, 1):
#         if (n % i == 0):
#             print(n,"is not a prime no")
#             return
#     print("is a prime nujmber")   

# n = int(input("Enter the no: "))
# prime(n)

## ques 3

# def getString(s1):
#     print(s1)
    
# def reverse(s1):
#     print(s1[::-1])
    
# s1 = input("Enter the sentence: ")
# getString(s1)
# reverse(s1)

""" dict ques 1 """

# dict_1 = {}
# n = int(input("Enter the no: "))
# for i in range(n):
#     key = input("Enter the name: ")
#     value = int(input("Enter the marks: "))
    
#     dict_1[key] = value
    
# print(dict_1)

# highest_scorer = "" # to get the topper
# highest_score = -1 # take it as low to get the max score get by student

# for student, marks in dict_1.items():
#     if marks > highest_score:
#         highest_score = marks
#         highest_scorer = student
        
# print(f"Student {highest_scorer} gets max marks i.e {highest_score}")     

## ques 2

# sentence = input("Enter the string: ")
# word = sentence.split()
# print(word)

# null_dict = {}

# count = 0
# key = input("Enter the word to find: ")

# for char in word:
#     if(key == char):
#         count += 1
        
# if count > 0:
#     print(f"'{key}' found {count} times")
# else:
#     print("key don't get count")
    
## ques 3 

# phoneBook = {}
# n = int(input("Enter the no of contacts: "))
# for i in range(n):
#     key = input("Enter the name of person: ")
#     value = int(input("Enter their phone no: +91-"))
    
#     phoneBook[key] = value
    
# for i in range(2):
#     key = input("Enter the contact: ")
#     value = int(input("Enter the no: +91-"))
#     phoneBook.update({key : value})

# search = input("Enter the contact to search: ")  
# phoneBook.get(search)
# print(phoneBook.get(search))

# pop = input("Enter contact to delete: ")
# if pop in phoneBook:
#     phoneBook.pop(pop)
# else:
#     print("Contact don't exist")

# print(phoneBook)

""" OOP's Concept """

# class Rectangle:
    
#     def AreaofRect(length, breadth):
#         return length * breadth
    
#     def Perimeter(length, breadth):
#         return 2*(length + breadth)
    
# # n = int(input("no of elements to get: "))
# # for i in range(n):
# length = float(input("Length: "))
# breadth = float(input("Breadth: "))
# length1 = float(input("Length: "))
# breadth1 = float(input("Breadth: "))


# r1 = Rectangle
# print("Area:",r1.AreaofRect(length, breadth))
# print("Perimeter:",r1.Perimeter(length, breadth))

# r2 = Rectangle
# print("Area:",r2.AreaofRect(length1, breadth1))
# print("Perimeter:",r2.Perimeter(length1, breadth1))


## constructor

# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
        
#     def display(self):
#         print("Title of the book:",self.title)
#         print("Author of the book:",self.author)
#         print("Pages of the book:",self.pages)

# #instances
# title = input("enter the title: ")
# authr = input("Enter the name of author: ")
# pages = int(input("Enter the no of pages: "))

# b1 = Book(title,authr,pages)
# b1.display()

## inheritence

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
        
#     def getdetails(self):
#         print("Name: ",self.name)
#         print("Salary:",self.salary)
        
# class Manager(Employee):
#     def __init__(self, name, salary,department):
#         self.department = department
#         super().__init__(name, salary)
    
#     def getdata(self):
#         self.getdetails()
#         print("Deaptment:",self.department)
        
# name ="Harsh"
# salary = 12315634.98
# department = "CSE"

# obj = Manager(name,salary,department)
# obj.getdata()

# name1 = "Daksh"
# salary1 = 11111111111111.09
# deprt = "IT"

# m1 = Manager(name1,salary1,deprt)
# m1.getdata()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     def get_details(self):
#         """Print the employee's details."""
#         print("Name: ", self.name)
#         print("Salary: $", format(self.salary, '.2f'))  # Format salary to 2 decimal places
        
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)  # Call the parent class constructor
#         self.department = department
    
#     def get_data(self):
#         """Print the manager's details, including department."""
#         self.get_details()  # Call the parent class method to get employee details
#         print("Department: ", self.department)

# def main():
#     # Get the number of managers to create
#     num_managers = int(input("Enter the number of managers: "))
    
#     # List to hold manager objects
#     managers = []
    
#     for _ in range(num_managers):
#         # Get details for each manager from user input
#         name = input("\nEnter manager's name: ")
#         salary = float(input("Enter manager's salary: "))
#         department = input("Enter manager's department: ")
        
#         # Create a Manager object and append to the list
#         manager = Manager(name, salary, department)
#         managers.append(manager)

#     # Display details for each manager
#     print("\nManager Details:")
#     for manager in managers:
#         manager.get_data()  # Call method to display manager details

# # Run the main function
# if __name__ == "__main__":
#     main()


## Encapsulation

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass ## private attr by using __ in variable name
        
    # def reset_pass(self):
    #     print(self.__acc_pass)
        
# acc_no = input("Enter the account no: ")
# acc_pin = int(input("Enter your pin: "))

# acc1 = Account(acc_no, acc_pin)
# print(acc1.acc_no)
# # print(acc1.__acc_pass) # error
# acc1.reset_pass()

# class BankAcc:
#     def __init__(self,balance):
#         self.__balance = balance
        
#     def getbalance(self):
#         return self.__balance
    
#     def deposit(self,deposit):
#         self.__balance += deposit
#         return self.__balance
    
#     def withdraw(self,withdraw):
#         if withdraw > self.__balance:
#             print("Insufficient Balance")
#         else:
#             self.__balance -= withdraw
#             return self.__balance
    
# balance = 10000
# deposit = 4000
# withdraw = 5500

# p1 = BankAcc(balance)
# print(p1.getbalance())
# print(p1.deposit(deposit))
# print(p1.withdraw(withdraw))

## polymorphism



# list_1 = []

# for i in range(6):
#     no = int(input("Enter the no: "))
#     list_1.append(no)
    
# print(list_1)
# odd_sum = 1

# for num in list_1:
#     if num % 2 != 0:
#         odd_sum *= num
        
# print(odd_sum)

# class CharacterCategorizer:
#     def __init__(self, char):
#         self.char = char

#     def categorize(self):
#         # Check if it's a valid single character
#         if len(self.char) != 1:
#             return f"'{self.char}' is an invalid input."
        
#         # Check for alphabets
#         if self.char.isalpha():
#             if self.char.lower() in 'aeiou':  # Check for vowels
#                 return f"'{self.char}' is a vowel."
#             else:  # If it's an alphabet but not a vowel, it's a consonant
#                 return f"'{self.char}' is a consonant."
#         # Check for special characters
#         elif self.char in '!@#$%^&*()_+-=[]{}|;:\'",.<>?/`~\\1234567890':
#             return f"'{self.char}' is a special character."
#         # If it's not an alphabet or special character, it's invalid
#         else:
#             return f"'{self.char}' is an invalid input."

# # Testing the class
# n = int(input("How many characters would you like to categorize? "))
# for i in range(n):
#     char_input = input("Enter a character: ")
#     categorizer = CharacterCategorizer(char_input)
#     result = categorizer.categorize()
#     print(result)

## diamond star pattern 

# Function to print a diamond pattern of stars
# def print_diamond(n):
#     # Print the upper part of the diamond
#     for i in range(n):  # Loop for each row of the upper part of the diamond
#         # Print spaces before the stars to center them
#         for j in range(n - i - 1):  # Loop to print the spaces
#             print(" ", end=" ")  # Print a space and stay on the same line
#         # Print stars for the current row
#         for k in range(2 * i + 1):  # Loop to print the stars
#             print("*", end=" ")  # Print a star and stay on the same line
#         print()  # Move to the next line after finishing the row of stars

#     # Print the lower part of the diamond (inverted pyramid)
#     for i in range(n - 2, -1, -1):  # Loop for each row of the lower part, starting from n-2 down to 0
#         # Print spaces before the stars to center them
#         for j in range(n - i - 1):  # Loop to print the spaces
#             print(" ", end=" ")  # Print a space and stay on the same line
#         # Print stars for the current row
#         for k in range(2 * i + 1):  # Loop to print the stars
#             print("*", end=" ")  # Print a star and stay on the same line
#         print()  # Move to the next line after finishing the row of stars

# # Input the number of rows for the diamond from the user
# n = int(input("Enter the number of rows for the diamond: "))  # Convert the input to an integer

# # Call the function to print the diamond pattern
# print_diamond(n)  # Pass the user input as the number of rows for the diamond

def process_string(user_input):
    # Initialize an empty string to store valid characters
    cleaned_string = ""
    
    # Loop through each character in the input string
    for char in user_input:
        # If the character is a letter (alphabet), add it to cleaned_string
        if char.isalpha():
            cleaned_string += char
    
    # Convert the cleaned string to uppercase and print it
    print(cleaned_string.upper())#string after removing the special or numeric values in a string

# Main program to take user input and call the function
user_input = input("Enter a string: ")
process_string(user_input)
