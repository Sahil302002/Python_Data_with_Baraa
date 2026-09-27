# String functions type

# name = "Sahil"
# print(type(name))
 
# age = 24
# print(type(age))

# print("Your Age is: "  age)
# This is giving type error so we will use str() function

# print("Your Age is: " + str(age))

# Math
# password = " 123a4d"
# print(len(password))

# if len( password) < 8:
#     print("Your Password is too short!")

# text = """ 
# Python  is easy to learn
# python is Powerful.
# Many people love python.
# """

# print(text.count("Python"))

# price = "1234,56"
# print(price.replace(",","."))

# phone = "176-1234-56"
# print(phone.replace("-","/"))

# phone = "176-1234-56"
# print(phone.replace("-"," "))


# price = "$1,299.99"
# print(price.replace("$","").replace(",",""))


# # Join Strings
# first_name = "Michael"
# last_name = "Scott"
# full_name = first_name + " " + last_name
# print(full_name)

# folder = "C:/Users/Baraa"
# file = "report.csv"
# full_file_path = folder + "/"+file
# print(full_file_path)

name = "Sam"
age = 14
is_student = False

#Old Approach
# print("My name is " + name + ", I am " + str(age) + " years old and student status is " + str(is_student) + ".")

# print(f"My name is {name}, I am {age} years old and student status is {is_student}.")

# print(f"2 + 3 = {2 + 3}")

# print(f"{This is me}")
# NameError: name 'This' is not defined

# print(f"{{This is me}}")
#! Anything inside {} in an f-string is evaluated, not printed literally.

#Split function

# stamp = "2026-09-20 14:30"
# print(stamp.split(" "))


# stamp = "2026-09-20"
# print(stamp.split("-"))


# csv_file = "1234,USA,1970,1950-10-05,M"
# print(csv_file.split(","))

# print("ha"*3)

# print("=" * 40)

# Exercise
# number = "+49 (176) 123-4567"

# print(number.replace("+","").replace("-","").replace(" ","").replace("(","").replace(")",""))

# Indexing and Slicing 
# text = "Python"
# print(len(text))
#Extract first character
# print(text[0])
# print(text[-6])
# print(text[-3])
# print(text[3])

#! negative_index = positive_index - len(string) 

# Extract last character
# print(text[-1])
# print(text[5])

# Extract h character
# print(text[3])
# print(text[-3])


date = "2026-09-20"

# Extract only year
# print(date[0:4])
# print(date[:4])  # Its just a lazy way


# Extract Month
# print(date[5:7])

# Extract the Day
# print(date[8:])
# print(date[-2:])


# text = " Engineering"
# print(text.lstrip())


# text = "Engineering  "
# print(text.rstrip())

# text = " Engineering  "
# print(text.strip())

# text = "$$$$$Engineering$$$$"
# print(text.strip('$'))

# text2 = "@Sahil302002@"
# print(text2.strip('@'))


# text = "   Engineering "
# print(len(text))
# print(len(text.strip()))

# nr_of_spaces = 10
# is_clean = 'No'
# print(f"No of spaces: {nr_of_spaces}")
# print(f"Is My data clean?: {is_clean}")

# Case Conversion 
# text = "python Programming"

# print(text.lower())
# print(text.upper())

# # Example
# search = "Email ".lower().strip()
# data = "emAil".lower().strip()
# print(search == data)

# Python Challenge: Advance Challenge:
# Turn the messy string into a single clean summary with name, role and age
# Clean String: name: maria role: data engineer  age: 27


# Task = "968- Maria, ( D@t@ Engineer ) ;; 27y "

# #My_Solution
# Task2 = Task.replace('-',"").replace(';','').replace('(',"").replace(')',"").replace('@','a').replace('y','').replace(',','')
# print(Task2.split(" "))
# name = Task2.split(" ")[1]
# Age = Task2.split(" ")[7]
# Role = Task2.split(" ")[3]  + " "+ (Task2.split(" ")[4])

# print(f"Name: {name} | Role: {Role} | Age: {Age}")
#Solution
# x = Task.replace("-","").replace("(","").replace(")","").replace(";;","").replace("@","a").replace("y","").replace(",","").split(' ')
# print(x)


# name = x[1]
# role = x[3] + ' ' + x[4]
# year = x[-2]
# print(f"Name: {name} | role = {role} | year = {year}")


# Search 
# Is the phone German? Check Country code(+49)
# phone = "+49-176-12345"
# print(phone.startswith("+49"))

# Is the email from Gmail? Check the Domain(gmail.com)
# email = "baraa@gmail.com"
# email = "baraa@outlook.com"

# print(email.endswith('gmail.com'))

# # Is the file a CSV? Check the extension

# file = "date_backup.csv"
# print(file.endswith(".csv"))

# Is this a valid email? Check for (@)
# print("@" in email)

# Check if the URL is an API endpoint
# url = "https://api.company.com/v1/data"

# print("/api" in url)

# Extract Only Phone number without country code
# phone1 = "+49-176-12345"
# phone2 = "48-654-16548"
# phone3 = "0048-654-16548"

# print(phone1[4:])
# print(phone2[3:])

# We use find to make Code more Dynamic
# print(phone2[phone2.find("-")+1:])
# print(phone1[phone1.find("-")+1:])
# print(phone3[phone3.find("-")+1:])

# Vaidation:
# Check if the country name contains only letters

# Code = "USA"
# print(Code.isalpha())

# Check if Phone number has having only numbers
# phone  = "01761234587"
# print(phone.isnumeric())

# phone  = "3.25"
# print(phone.isnumeric())


# phone  = "01761-234587"
# print(phone.isnumeric())