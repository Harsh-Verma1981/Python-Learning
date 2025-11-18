""" Intro to Function """

def SumofVal(a, b):# func declratn and defintn
    Total = a + b
    return Total

# function calling
x = int(input("Enter val1: "))
y = int(input("Enter val2: "))
print("The sum of func var =",SumofVal(x, y))


def say_Hello(): # hello func
    str = "Hello"
    return str

for i in range(4):
        print(say_Hello())
        

def average(a,b,c):
    avg = (a+b+c)/3
    return avg

x = int(input("Enter the no: "))
y = int(input("Enter the no: "))
z = int(input("Enter the no: "))

print(average(x,y,z)) 


list = [1,2,3,4,5]
def len_list(list):
    print(len(list))
    # return
    
print(len_list(list))


def average(a):
    if(a % 2 == 0):
        print("Even ")
    else:
        print("Odd!")
        
    return 

x = int(input("Enter the no: "))

# func call
print(average(x))


""" Recursion """

def display(n):
    if(n == 7): # base condition
        return
    print(n)
    display(n + 1)
    
display(1)

def fact(n):#declr and define
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)
    
no = int (input("Enter the no of terms: "))
fact(no) # function calling 

print(fact(no))

""" Question """

def getSum(n):
    if (n == 0):
        return 0
    else:
        return n + getSum(n - 1)
    
a = int(input())
# func call
getSum(a)

print(getSum(a))

def display(list, idx = 0):
    if idx == len(list):
        return 
    print(list[idx])
    display(list, idx + 1) # callling the func without print

list_no = [1, 2, 34, 5, 6]
display(list_no)

