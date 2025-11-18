""" Dictionary """

dict = {
    "name" : "Harsh",
    "last_name" : "Verma",
    "reg_no" : 123,
    "cgpa" : 7.6,
    "fees" : True,
    "subjects" : ["DSA", "C++", "Python", "OS", "networks"]
}

print(type(dict))
print(dict)

"""by input """

null_dict = {}
null_dict["name"] = "Ajay Verma" # dict is mutable 

# by input from user

n = int(input("Enter the menbers: "))

for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the valur to add: ")
    null_dict[key] = value
 
print(null_dict)

""" Nested dict """

student = {
    "Name" : "Daksh",
    "subjects" : {
        "phy" : 89,
        "chem" : 98,
        "math" : 88 
    }
}

# print(student)
print(student["subjects"]["chem"])

""" Dict methords """

student = {
    "Name" : "Daksh",
    "subjects" : {
        "phy" : 89,
        "chem" : 98,
        "math" : 88 
    }
}

print(student.keys()) # return the keys only

""" by typecasting
 print(list(student.keys())) # converted into list from dict
"""

print(len(student))
print(list(student.values())) # return all values of dict
print(student.items()) # return as tuple
print(student.get("Name"))

student.update({"city" : "Delhi", "age" : "15"})#to add new key and value in a dict
print(student)

""" Sets """

nums = {1,2,3,2,3,"hii","harsh","harsh"}# remove duplicates by itself 

print(len(nums))
print(nums) # 1 2 3 hii harsh

null_set = set() #empty set syntax
print(type(null_set))

""" Sets methord """

nums = set()
nums.add(1)
nums.add(2)
nums.add(3)

print(nums)

nums.remove(2)
nums.add([2,4])# error 

nums.clear()

nums.pop() # removes random value by itself
print(nums)

nums_1 = {1,2,3,4}
nums_2 = {3,4,5,6}

union = nums_1.union(nums_2) # gives the union of both sets
print(union)

intersct = nums_1.intersection(nums_2) # gives the inserction of both sets
print(intersct)

""" Question """

dict = {
    "table" : "a peice of furniture", 
    "cat" : "an animal"
}
# print(dict)
dict["table"] = "a way to represent the multiples of no's in maths"
# print(dict)
dict["dog"] = dict.pop("cat")
print(dict)


subjects = {"java","C++","c","python","c++","java","pyhton"}
print("total no of classrooms are ", len(subjects))


stud_marks = {}

n = int(input("enter: "))

for i in range(n):
    subj = input("enter the subject: ")
    marks = input("enter the marks: ")
    
    stud_marks[subj] = marks
    
print(stud_marks)


val1 = int(input("val1 = "))
val2 = input("val2 = ")

set = {val1, val2}
print(set)
