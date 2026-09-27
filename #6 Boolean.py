print(True)
print(False)
print(type(True))
print(bool(123))
print(bool((-1)))
print(bool(("hi")))
print(bool()) # False
print(bool(0)) # False
print(bool("")) # False
print(bool(None))# False
# bool(value):Built-in function, Output:boolee
#! True: if the values is non-empty or non-zero
#! False: if the value is empty or zero

# {True, False, False} If we put all these value together And we want python evaluate them all together
# any: Return True if atleast one value is True
# all: Return True if all value is True   eg., If there is somewhere false it will return false

email = ""
phone = "0176-123456"
username = ""
#Allows Registration if Any field is filled

print(any([email, phone, username]))

#Allows Registration if All field is filled


email = "sahil123@gmail.com"
phone = "0176-123456"
username = "Sahil123"
print(all([email, phone, username]))

#isinstance(value,type): built-in function Output:Bool
#Check if a value belongs to certain Data type 

print(isinstance("Hi",int))
print(isinstance(1234,int))
print(isinstance(True,str))

print(isinstance(True,int))

# True behaves like the integer 1
# False behaves like the integer 0
#! Python says — “Yes, because bool is a subclass of int.”

# endswith(substring) str:Method output:bool
# Checks if the strings end with specific string
print("Hello".endswith("o"))
print("Hello".startswith("H"))

# Comparison Operators: 
# It Compares two values and return True or False based on the result.

print(10==10)
print(10!=10)
print(7>3)
print(7>=10)
print(7<7)
print(7<=7)

# Strings can be compared too!
# You can compare strings too alphabetically, not just numbers

print("a">"b")
print("a"=="b")
print("d">"b")

# Python is Case Sensitive: So "a" and "A" are treated as different values
print("a"=="A")

# Don't mix them up!
# = Assigns, == Compares

# Chained Comparison:Check Multiple in one line, just like in math
# It evaluates it from left to right, checking each condition one by one
# Chained Comparisons work like SQL's Between They if a value is between two bounds
print(1 < 4 < 6) # Like here python is checking if 4 lies between 1 and 6

# Is Age between 18 and 30?
age = 55
print(18 <= age <=30)

# Logical Operators: Used to Combine Multiple booleans

print(4<3 and 7<5)
print(4>3 and 7>5)


print(4<3 or 7>5)
print(4>3 or 7<5)
print(4<3 or 7<5)

# Checks if the system is under pressure
cpu_usage = 70
memory_usage = 95

print(cpu_usage >90 or memory_usage>90)

#Checking user credentials before login
email = False 
password = False

print(email and password)

# Not Operator: It Reverses the Truth it turns True into False and False into True
print(not 3>2)

print(not 3<2)
print(not True)
print(not False)

print()
print(not not True)
name = ""

print(not name) # Here Remeber that Bool of "" is False and here we have put "not" so we will get true

print(not 0)

# Controlled Mixed Conditions

# And Operator has Higher than OR
print(5==5 or 8>5 and 6<4)
# Use paranthesis to Control the Execution order

print((5==5 or 8>5) and 6<4)

# Allow Access only if the user is logged in or they are guest but they must not banned
is_logged_in = True
is_guest = False
is_banned = True

# This Case would be incorrect, Because first thing we have to check is Loggedin or is guest then we have to check it is banned or not
# print(is_logged_in or is_guest and not is_banned)

# Solution2
print((is_logged_in or is_guest) and not is_banned)

# Task1 Check if the user name is not empty and the age is greater than or equal to 18
username = ""
age = 15

# print(not username == "" and age >= 18) # My solution 
print(username != "" and age >=18)



# Task2: Check if the password is atleast 8 Characters long and does not contain spaces

password ="2536241 24"

# print(len(password)>=8 and bool(password.find(" "))) # My Solution
print(len(password) >= 8 and " " not in password)

# Task3 : Check if a user's email is not empty, contains "@", and ends with ".com"

user_email = "baraa123@gmail.com"

print(user_email != "" and "@" in user_email and user_email.endswith(".com")) # Correct

# Task4: Check if a username is a string, is not None, and is longer than 5 characters
username = "Sahil"

print(isinstance(username,str) and username != None and len(username)> 5) # One mistake its says longer so it will be >5 and not >=5

# Task5: Check if the user is either an admin or a moderator, and either they’re not banned or they’ve verified their email
user = "Admin"
is_banned = True
is_verified = False

print((user == "Admin" or user == "Moderator") and (not is_banned or is_verified))

# Membership & Identity operator

# In Operator
# Checks if the Value is inside the other value
# like string,list, tuple, or other sequence 

print("o" in "Python")

print("p" in "python")

print("f" not in "python")

print(3 in [1,2,3])

# Task: Validate that the domain is not on the banned list

#Security check insure that domain is not banned
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)
"""
Identity Operators(is - is not)
Checsk if two variables refer to the same object in memory


Identity Operators
Purpose: Identity operators are used to check whether two variables are referring to the same object in memory. They are concerned with the "identity" of objects, not just their values.
Operators: There are two identity operators:
  is: Checks if two variables have the same identity, meaning they point to the same object ID in memory.
  is not: Checks if two variables do not point to the same object ID in memory.

Comparison with the Equality Operator (==)
 == (Equal Operator): Compares the values of the two variables. For instance, if a = [1,2,3] and b = [1,2,3], then a == b would yield true because their values are identical.

 is (Identity Operator): Compares the IDs of the objects that the variables point to in memory. It determines if they are literally the same object. If a = [1,2,3] and b = [1,2,3], a is b would return false because Python typically creates two distinct objects in memory for complex values, each with a different ID.

Python's Memory Model and Object Identity
Variable Storage: In Python, variables do not directly store values. Instead, they point to an object ID in memory. Each object in memory has a unique ID and a corresponding value. This means variables are connected to objects using "pointers".

How is Works: When a is b is evaluated, Python compares the IDs of the objects that a and b point to. It does not care about the values themselves in this operation.
"""
x = ['a','b','c']
y = ['a','b','c']

print(x==y)

print(x is y)

print()
x = 5
y = 5

print(x==y)

print(x is y)
print()


x = ['a','b','c']
y = x

#here "=" Between two variables, Assigns one variable to the same object that another variable 
print(x==y)

print(x is y)

# Validate the email address It must be filled in and not empty
#Task: Make sure the email exist and its not empty

# email = "b@gmai.com"
# print(email !="")

# But some time there is None, None means No value at all, it is Unknown,
#  ""- Means an empty but is known, its is string

email = None
print(email !="" and email != None)

# Use is instead of == when working with None as a best practices of coder or developer and anyway its not going to create any difference


email = None
print(email !="" and email  is not  None)

