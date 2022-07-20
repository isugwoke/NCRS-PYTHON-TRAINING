from operator import le


mystr = 'Mike'
my_info = "I am a python developer"
sms_code = "123wer#@2uyTTh"
num_str = '23'
comment = "I'm becoming very good at python"

# print(mystr)
# print(my_info)
# print(sms_code)
# print(comment)

# String indexing and slicing
# Indexing
str = "abcdedgh"
# print(str[0])
# print(str[3])

# Reverse Indexing
# print(str[-3])

first_letter = str[0]
last_letter = str[-1]

# print(first_letter)
# print(last_letter)

# String Slicing
my_name = "Abdullahi"

print(my_name[:3]) #output: Abd
print(my_name[:4]) #Output: Abdu
print(my_name[2:]) #Output: dullahi
print(my_name[2:6]) #Output: dull
print(my_name[5:8])  #output: lah

# String concatenation
str1 = 'a'
str2 = 'b'
str3 = 'c'
# print(str1 + str2) #output: ab

greeting = "Good morning"
name = 'Tony'
feature = 'you are awesome'

# Task: print: Good morning Tony you are awesome

print(greeting + " " + name)
print(greeting + " " + name + " " +feature)
# print(greeting + name) #Good morningTony

# print("2" + "4")
# print("a" * 5)

# String Formatting

# age = current year - birth year
name = 'Tony'
birth_year = 1980
age = 2022 - birth_year  #age = 50
print(age)

# Hello Tony you were born in birth_year, your age is 50
print(f"Hello Tony you were born in {birth_year}, your age is {age}")

# Strings are immutable
str = "Sam"
# I want to change Sam to Pam

print("P" + str[1:]) #output: Pam

# String Methods
name = "obong"

# upper - Returns the uppercase of a string
name_capitals = name.upper()
# print(name.upper())
print(name_capitals)

# lower
name2 = "MIcHAEL"
print(name2.lower())

# capitalize - Returns the  string with the first letter capitalized
print(name.capitalize())

# Accepting user input
# print(input("Enter your name "))

# user_name = input("Enter your name ")
# next_of_kin = input("Enter next of kin's name: ")

# print("Good morning " + user_name + " Your next of kin is " + next_of_kin)

a = int(input("Enter a: "))
b = int(input ("Enter b: ")) 

c = a + b

print(c)




