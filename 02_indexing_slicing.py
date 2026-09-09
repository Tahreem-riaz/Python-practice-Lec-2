"""
========================================================
      LECTURE 02 - FILE 2: INDEXING & SLICING
========================================================
Topics: Indexing, Slicing, Negative Indexing,
        Negative Slicing
========================================================
"""

# ==========================================
# PART A: INDEXING
# ==========================================

# Q1. Store a programming language in a variable.
#
#     Print:
#     - First character
#     - Third character
#     - Last character

language = "Python"

print(language[0])    # First character
print(language[2])    # Third character
print(language[-1])   # Last character

# ------------------------------------------

# Q2. Use the following string:
#
#     word = "COMPUTER"
#
#     Access and print the characters at:
#     index 1
#     index 4
#     index 6
#
#     Then access the same positions using negative
#     indexes where possible.

word = "COMPUTER"

print(word[1])     # O
print(word[4])     # U
print(word[6])     # E

print(word[-7])    # O
print(word[-4])    # U
print(word[-2])    # E

# ==========================================
# PART B: SLICING
# ==========================================

# Q3. Create a string containing a full sentence.
#
#     Use slicing to extract:
#     - The first five characters
#     - A middle portion
#     - The last five characters

sentence = "Python is easy to learn"

print(sentence[:5])      # First five characters
print(sentence[7:13])    # Middle portion
print(sentence[-5:])     # Last five characters

# ------------------------------------------

# Q4. Store a word in a variable.
#
#     Use slicing with a step value to:
#     - Print every second character
#     - Print every third character
