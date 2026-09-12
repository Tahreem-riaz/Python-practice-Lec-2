"""
========================================================
    LECTURE 02 - FILE 4: CONDITIONAL STATEMENTS
========================================================
Topics: if, elif, else, Comparison and Logical
        Conditions
========================================================
"""

# ==========================================
# PART A: IF STATEMENT
# ==========================================

# Q1. Create a variable containing a person's age.
#
#     If the age is 18 or above, print:
#     "Eligible to vote"

age = 20

if age >= 18:
    print("Eligible to vote")

# ------------------------------------------

# Q2. Create a variable containing a temperature.
#
#     If the temperature is above 35, print:
#     "High Temperature"

temperature = 38

if temperature > 35:
    print("High Temperature")

# ==========================================
# PART B: IF-ELSE
# ==========================================

# Q3. Create a variable containing a student's marks.
#
#     If the marks are 50 or above, print "Passed".
#     Otherwise, print "Failed".

marks = 75

if marks >= 50:
    print("Passed")
else:
    print("Failed")

# ------------------------------------------

# Q4. Ask the user to enter a number.
#
#     Check whether the number is positive or negative.
#     Handle zero as well.

number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# ==========================================
# PART C: IF-ELIF-ELSE
# ==========================================
