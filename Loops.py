""" Intro to loop """
# # #  implementation of code 
""" while loop """

count = 1 # iterator 
while count <= 5:
    # end is use to print this in single line
    print("Hello", end="")
    count += 1
    
# exec of loop upto n time is iteration

print("\n",count)

""" star case pattern """

i = 1
n = 5
while i<=n:
    print("*" * i)
    i += 1 # increment the value of i 

""" Table of no """

i = 1
n = 10
no = int(input("Enter the number: "))

while i<=n:
    print(no * i)
    i += 1# increment

i = 1
n = int(input("enter: "))
tup = () # empty tuple

while i <= n:
    TupVal = int(input("Enter element: "))
    tup += (TupVal,)
    i += 1 # increment

# for tarversing the tuple
for i in range(n):
    print(tup[i])
     
# linear search algo

key = int (input("Enter the key: "))
found  = False

for i in range(n):
    if tup[i] == key:
        found = True
        break
    
# ckecking the condition
if found:
    print("key ", key," exist")
else:
    print("key not existed")

""" for loops """

nums = [1,2,3,4,5]
for val in nums:
    print(val)
else: # for loop else is optional in that case i.e it is also get execute
    print("END")

list = [];
i = 1
size = 5
for i in range(size):
    add = int(input("Enter the val: "))
    list.append(add)
    
print(list)

tuple = ()
i = 1
n = 5
for i in range(n):
    val = int(input("enter plz: "))
    tuple += (val,)
    
    
for i in range(n):
    print(tuple[i])
    
    key = 2
    if(tuple[i] == key):
        print(key)
        break
    else:
        print("key not found")

for i in range(2, 10): # 2 is giving the start val && 10 is giving the stop value 
    print(i) 
    
for i in range(2, 10, 2): # here 1st 2 is start val && 10 is last val && last 2 is step val
    print(i) 
