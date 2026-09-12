"""
========================================================
          LECTURE 02 - FILE 5: MINI PROJECT
========================================================
Project: Username & Password Validator

Concepts Used:
- Strings
- String Methods
- Escape Sequences
- Indexing
- Slicing
- String Functions
- Conditional Statements
========================================================
"""
print("=" * 50)
print("        USERNAME & PASSWORD VALIDATOR")
print("=" * 50)

# --------------------------------------------------------
# STEP 1: GET USER INFORMATION
# --------------------------------------------------------

# Ask the user to enter:
# - Username
# - Password

username = input("Enter your username: ")
password = input("Enter your password: ")

# --------------------------------------------------------
# STEP 2: CLEAN THE USERNAME
# --------------------------------------------------------

# Remove unnecessary spaces from the username
# and convert it to a consistent case.

username = username.strip()
username = username.lower()

# --------------------------------------------------------
# STEP 3: ANALYZE THE USERNAME
# --------------------------------------------------------

# Find:
# - Username length
# - First character
# - Last character
#
# Display the information.

username_length = len(username)
first_character = username[0]
last_character = username[-1]

print("\nUsername Information")
print("Username:", username)
print("Length:", username_length)
print("First character:", first_character)
print("Last character:", last_character)

# --------------------------------------------------------
# STEP 4: CHECK PASSWORD
# --------------------------------------------------------

# Create conditions to check whether:
#
# - Password has at least 8 characters
# - Password contains at least one number
#
# Display an appropriate message.

password_length = len(password)
has_number = any(character.isdigit() for character in password)

if password_length >= 8:
    print("\nPassword has at least 8 characters.")
else:
    print("\nPassword must have at least 8 characters.")

if has_number:
    print("Password contains a number.")
else:
    print("Password must contain at least one number.")


 # --------------------------------------------------------
# STEP 5: FINAL RESULT
# --------------------------------------------------------
# 
# # If the username and password satisfy your conditions,
# display a success message.
#
# Otherwise, display a suitable warning.   

if username_length > 0 and password_length >= 8 and has_number:
    print("\nValidation Successful!")
    print("Username and password meet the requirements.")
else:
    print("\nValidation Failed!")
    print("Please check your username and password.")

# --------------------------------------------------------
# EXTRA CHALLENGE
# --------------------------------------------------------

# Improve your validator by checking:
# - Password contains an uppercase letter
# - Password contains a lowercase letter
# - Password contains a special character
# - Username does not contain spaces

has_uppercase = any(character.isupper() for character in password)
has_lowercase = any(character.islower() for character in password)
has_special = any(not character.isalnum() for character in password)
username_has_spaces = " " in username

if has_uppercase:
    print("Password has an uppercase letter.")
else:
    print("Password needs an uppercase letter.")

if has_lowercase:
    print("Password has a lowercase letter.")
else:
    print("Password needs a lowercase letter.")

if has_special:
    print("Password has a special character.")
else:
    print("Password needs a special character.")

if username_has_spaces:
    print("Username should not contain spaces.")
else:
    print("Username does not contain spaces.")