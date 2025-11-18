""" List/Arrays """

size = int(input("Enter the size of an array: "))

# array but can store any datatype simultanesly
marks = [1,2,3,4,5,6] # list / array

print(type(marks))
print (marks)# traversing the element
print(len(marks))# len of arr
print(marks[4])# access element

""" List slicing """

marks = [1,2,4,5,6,5]
print(marks[1:-2])

""" List Methord """

list = [5,4,2]
list.append(7) # add val at end  """ it will give none if we use this func with print"""
print(list) 

list.sort() # for ascending order
print(list)

#for desc order

list.sort(reverse=True)
print(list)

#for reversing the array

list.reverse() 
print(list)

#insert at specific

#syntax list.insert(index, val)
list.insert(0, 6)
print(list)

#del at element only not position
list.remove(4)
print(list)

#remove element by index or position
list.pop(2)
print(list)

""" Tuples """

tup = (1,23,4,5,6)
print(type(tup))

tup1  = (1) # incorrect
print(type(tup1)) # it take it as int 

tup2 = (1,)
print(type(tup2))

""" Tuple Slicing """

tuple = (1,2,4,5,67,7)
print(tuple[2:4])

""" Tuples Methord """
tuple = (1,2,4,5,6,7,7,7)

indx = tuple.index(4) # 4 is element present in it  not an index val
count = tuple.count(7) # count of duplicate element

print(indx)
print(count)
print(tuple)

""" Question """

my_list = []

size = int(input("Enter the size for list: "))

for i in range(size):
    movie = input("enter the name of movie: \n")
    my_list.append(movie)
    
# print the name of movies
print("The movies are ", my_list)


my_list1 = []

size = int(input("Enter the size for list: "))

for i in range(size):
    val = input("enter the value = ")
    my_list1.append(val)
    
# print(my_list1)

list = my_list1.copy()
list.reverse()
# print(list)

print("The output is ")

if(my_list1 == list):
    print("Yes, it is Palindrome ")
else:
    print("Sorry try again")
