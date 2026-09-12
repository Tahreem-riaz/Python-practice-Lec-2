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
