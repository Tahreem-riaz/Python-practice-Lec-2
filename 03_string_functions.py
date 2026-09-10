"""
========================================================
       LECTURE 02 - FILE 3: STRING FUNCTIONS
========================================================
Topics: String Functions and String Operations
========================================================
"""

# ==========================================
# PART A: LENGTH & CHARACTER INFORMATION
# ==========================================

# Q1. Create a string containing the name of a
#     programming language.
#
#     Find and print the number of characters in it
#     using len().

language = "Python"

print(len(language))

# ------------------------------------------

# Q2. Create a sentence.
#
#     Use len() to find its length.
#     Print the sentence and its length.

sentence = "I am learning Python"

print(sentence)
print(len(sentence))

# ==========================================
# PART B: SEARCHING & COUNTING
# ==========================================

# Q3. Create a sentence containing a word multiple
#     times.
#
#     Find:
#     - How many times the word appears
#     - The position where the first occurrence starts
#
#     Print both results.

sentence = "Python is easy. I love Python because Python is useful."

print(sentence.count("Python"))
print(sentence.find("Python"))

# ------------------------------------------

# Q4. Create a string containing an email address.
#
#     Use an appropriate function or operation to
#     check whether it contains the "@" symbol.
