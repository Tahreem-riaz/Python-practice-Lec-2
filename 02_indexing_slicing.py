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
