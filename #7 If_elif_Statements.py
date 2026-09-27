"""
Conditional Statments

Check point that checks a condition
- True? Runs the Code
- False? Skip it

If Statements: 
Defines the first condition if this is true do this  - Otherwise, do nothing

Rules
(1) Only One If Statement for each chain
(2) Starts with if
(3) If You are building Conditional statements if is required
(4) It can standalone

"""
score = 100
if score >= 90:
    print("A")

"""

! Indentation
Adding spaces at the beginning of a line to show that the line belongs to a code block

Acccording to PEP 8 - Style Guide: Use 4 spaces per indentation Level.

Configure the Visual Studio to always add four spaces automatically 
Ctrl + Shift+ P > Preferences: Open user settings

Two-Way Decision
 IF - Else

!Else Statement
Runs only if all Previous conditions are false
"if nothing was true do this instead"

If condition1:
    do A
else:
    do B

Rule

"""
marks = 55
if marks >= 80:
    print("Pass")
else:
    print("Fail")

"""
! Else Rules:
(1) Comes at the End
(2) No Conditions
(3) Optional
(4) Cannot stand alone 
(5) Only one else

Note: Else Cannot be use on its own

"""

marks = 55
if marks >= 80:
    print("Pass")
else:
    print("Fail")

"""
! Multiple Conditions
If-else-else

Elif Statement
Asks a followup question Only runs if previous conditions were false 

"If the first wasn't true this one"

if condition1:
    do A
elif Condition2
    do C
else:
    do B
"""

"""
!Elif Rules
(1) Comes After if
(2) Multiple elif
(3) Needs Condition
(4) Optional
(5) Cannot Standalone
 

"""
# if-elif-else

marks = 30
if marks >= 80:
    print("A")
elif marks >= 55:
    print("B")
else:
    print("D")

# if-elif-elif-else

marks = 30
if marks >= 80:
    print("A")
elif marks >= 55:
    print("B")
elif marks >= 35:
    print("C")
else:
    print("D")

"""
 Nesting IF Else

If Statement inside another if 
"If the first is true then check the Second"
 
Each if can be followed by Else

"""

marks = 85

Submitted_Project = False

if marks >= 80:
    if Submitted_Project:   # Python evaluates Boolean conditions directly Avoid explicit comparisons == True or == False
        print("A+")
    else:
        print("A")
elif marks >= 55:
    print("B")
elif marks >= 35:
    print("C")
else:
    print("D")

"""
!Connecting Conditions: Logical Operators

"""

marks = 59
Submitted_Project = False

if marks >= 90 and Submitted_Project:  
    print("A+")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60 or Submitted_Project:
    print("D")
else:
    print("F")

"""
!Independent If-else Statement

Each if is checked separately 
"All Conditions are tested - even if one  is already true"



Example
"""
marks = 92
Submitted_Project = True

if marks >= 90:
    print("High Score")
else:
    print("Low Score")

if Submitted_Project:
    print("Project is submitted")
else:
    print("Project is not submitted")

"""
!Python Challenges
Validate the Quality and Correctness of Email values
(1) Must not be empty
(2) Must contain "." and "@"
(3) Must contain exactly one "@" symbol
(4) Must end with ".com",".org",".net"
(5) Must not be longer than 254 characters
(6) Must start and end with a letter or digit
"""
#  Here if email is " " clean the email 


email = "sahilgupt@gmail.com"
# Clean the String
email = email.strip()

# Email must not be empty
if email =="":
    print("Email cannot be empty.")
# Email must contain a "." and "@"
elif not('.' in email and '@' in email):
    print("Email must contain . and @")
# Email Must contain exactly one "@" symbol
elif email.count('@') !=1:
    print("Email must contain exactly one @")
# Email Must end with ".com",".org",".net"
elif not email.endswith(('.com','.net', '.org')):
    print("Email Must end with .com,.org,.net")
# Email Must not be longer than 254 characters
elif len(email) > 254:
    print("Email Must not be longer than 254 characters")
# Email Must start and end with a letter or digit
elif not(email[0].isalnum() and  email[-1].isalnum()):
    print("Email Must start and end with a letter or digit")
else:
    print("Email is valid")

# isalnum()- Checks if the string contains only letters and digits

# Basic approach 
#? elif email.endswith('.com') or email.endswith('.net') or email.endswith('.org'):


# Email Must end with ".com",".org",".net"
#? elif email.endswith('com'or '.org' or '.net'):
#     print("Email Must end with .com,.org,.net")


if (email != '' and email != None) and ('.' in email and '@' in email) and (email.endswith(".com" or ".net" or".org")) and not len(email)>=254:
    print("Ok Email")


"""
!Note
You want to stop at the first condition that returns True?
If-elif-else

You want all conditions to be evaluated ?
Independent if statements

"""


email = "Sahil.gupta@.org"
# Clean the String
email = email.strip()
valid = True

# Email must not be empty
if email =="":
    print("Email cannot be empty.")
    valid = False
# Email must contain a "." and "@"
if not('.' in email and '@' in email):
    print("Email must contain . and @")
    valid = False
# Email Must contain exactly one "@" symbol
if email.count('@') !=1:
    print("Email must contain exactly one @")
    valid = False
# Email Must end with ".com",".org",".net"
if not email.endswith(('.com','.net', '.org')):
    print("Email Must end with .com,.org,.net")
    valid = False
# Email Must not be longer than 254 characters
if len(email) > 254:
    print("Email Must not be longer than 254 characters")
    valid = False
# Email Must start and end with a letter or digit
if not(email[0].isalnum() and  email[-1].isalnum()):
    print("Email Must start and end with a letter or digit")
    valid = False
if valid:
    print("Email is valid")

"""
2 Validate the Quality and Correctness of Passwords
Must not be empty
Must be at atleast 8 Characters
Must Include at least 1 Uppercase
Must include at least 1 Lowercase
Must not be same as the email
Must not contains any spaces
Must start and end with a letter or digit
"""

email = "Sahilgupta30303@gmail.com"
password = "S sdfg@1234"

password = password.strip()
if password =="":
    print("password must not be empty")
elif len(password)<= 8:
    print("password must include atleast 8 characters")
elif  not(any(char.isupper() for char in password)):
    print("Must Include at least 1 Uppercase")
elif  not(any(char.islower() for char in password)):
    print("Must Include at least 1 lowercase")
elif password == email:
    print("Password Must not be same as the email")
elif password.count(" ") != 0:
    print("Password Must not contains any spaces")
elif not(password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")
else:
    print("Its ok")



# Independent If conditions

email = "Sahilgupta30303@gmail.com"
password = "Sg@1234"

valid = True

password = password.strip()
if password == "":
    print("Password must not be empty")
    valid = False
if len(password) < 8:
    print("Password must include at least 8 characters")
    valid = False
if not any(char.isupper() for char in password):
    print("Password must include at least 1 uppercase")
    valid = False
if not any(char.islower() for char in password):
    print("Password must include at least 1 lowercase")
    valid = False
if password == email:
    print("Password must not be the same as the email")
    valid = False
if " " in password:
    print("Password must not contain spaces")
    valid = False
if not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")
    valid = False

if valid:
    print("✅ Password is ok")
