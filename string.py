""" String """

str1 = "Hii, I am a learning Python"
print(str1)

"""String concetenation"""

str = "Hello "
str_one = "World!"

concetnate = str + str_one
print(concetnate)
""" 
"""

"""length=len of string"""

str = "Hii this is my string lecture"
print(len(str))

length = len(str)
print(length)

"""Indexing of a string"""

str = "Harsh"
char = str[3]

print(str[0])
print(char)

""" Slicing """

str = "Hi Harsh"
print(str[3:len(str)])# to get the partclr char present in string
print(str[-5:-2])#negative slice

""" Sub string """

string = "this is a string tutorial"

print(string.endswith("rial"))# true or false
print(string.capitalize())# capitalize the 1st chr in string
print(string.replace("i", "o"))# to replace string or a single chr

print(string.find("a"))# to find string or a single chr
print(string.count(""))# to find the count of chr or string 
print(string.upper())

""" ques in python exam """

def process_string(user_input):
    # Initialize an empty string to store valid characters
    cleaned_string = ""
    
    # Loop through each character in the input string
    for char in user_input:
        # If the character is a letter (alphabet), add it to cleaned_string
        if char.isalpha():
            cleaned_string += char
    
    # Convert the cleaned string to uppercase and print it
    print(cleaned_string.upper())

# Main program to take user input and call the function
user_input = input("Enter a string: ")
process_string(user_input)
