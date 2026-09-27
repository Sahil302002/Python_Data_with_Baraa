"""!Inline if (Ternary)
Instead of this 
If Condition1:                 Inline if
    do A                       do A if condition1 else do B
else:
    do B
Eg.,
"A" if score>= 90 else "F"

!Rules
You cannot skip Else , You must include If and else in Inline if statement

Output is going to get stored in Variable
But this is for simple Logic!
"""

score = 100
# if score>= 90:
#     print("A")
# else:
#     print("F")

print("A" if score >= 90 else "F")


score = 65
# if score >= 90:
#     print("A")
# elif score>= 80:
#     print("B")
# else:
#     print("F")

grade ="A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)

"""
 Note Simple Logic = Inline-if
 Complex Logic = Classical-if

#! Special Statments: Match Case

Evaluate a value against multiple values Runs the Code of the First match

Taskl: Convert the full country names into 2- Letter abbreviation
"""

country = "USA"

if country =="United States":
    print("US")
elif country == "India":
    print("IN")
# elif country == "Germany":     For Flexible logic and multiple Conditions
    print("DE")
elif country == "Egypt":
    print("EG")
else:
    print("Unknown Country")

# Best Appraoch: This way is Easy to Read and Write 

match country:
    case "United States" | "USA":
        print("US")
    case "United States":
        print("US")
    case "USA":    # Can be used only for matching values
        print("US")
    case "Egypt":
        print("EG")
    case _:
        print("Unknown Country")

# Here we can use Pipe to match multiple values in single case

""" Summary of If Statements

If Starts the 1st Condition

elif: Adds a followup Condition if the previous is false

Else: "Fallback" if none of the conditions are met


Standalonge If statement: "Just for Checking", If this true do this - Otherwise, do nothing

If - else statement: "This or that"

If-elif-else Statement
"Branching"
"Choose one from many"

Nested If: "Layered Tree"
"Step-by-step decisions"

Independent If Statements: "Checklist Mode"
"Test all Conditions"

In-line if Statement
do A if conditionelse do B
"Quick, short and simple Check"


Case Match: "Pattern Matcher", "Match one Exact value to multiple options"


"""