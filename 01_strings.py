"""
========================================================
          LECTURE 02 - FILE 1: STRINGS
========================================================
Topics: Strings, String Methods, Escape Sequences
========================================================
"""

# ==========================================
# PART A: STRING BASICS
# ==========================================

# Q1. Create three strings representing:
#     - A book title
#     - An author's name
#     - A short description
#
#     Print all three strings.

book_title = "Python Programming"
author_name = "John Smith"
description = "A beginner-friendly book about Python programming."

print("Book Title:", book_title)
print("Author:", author_name)
print("Description:", description)

# ------------------------------------------

# Q2. Create the following sentence using a string:
#
#     Python makes programming interesting.
#
#     Print the sentence using both single quotes
#     and double quotes.

sentence1 = 'Python makes programming interesting.'
sentence2 = "Python makes programming interesting."

print(sentence1)
print(sentence2)

# ==========================================
# PART B: ESCAPE SEQUENCES
# ==========================================

# Q3. Print a small menu using escape sequences.
#
#     Your output should contain:
#     - A heading
#     - At least three items
#     - Tabs or spacing
#     - New lines
#
#     Use \n and \t.

print("===== MENU =====\n")
print("1.\tPython")
print("2.\tJava")
print("3.\tC++")
print("4.\tJavaScript")

# ------------------------------------------

# Q4. Create a string containing quotation marks
#     inside it.
#
#     Print a sentence similar to:
#
#     The teacher said, "Practice Python every day."
#
#     Use an appropriate escape sequence.

print("The teacher said, \"Practice Python every day.\"")

# ==========================================
# PART C: STRING METHODS
# ==========================================

# Q5. Create a string containing a person's name
#     with unnecessary spaces and mixed capitalization.
#
#     Use string methods to:
#     - Remove extra spaces
#     - Convert it to lowercase
#     - Convert it to uppercase
#
#     Print each result.

name = "   AlEx JoHn   "

clean_name = name.strip()
lowercase_name = clean_name.lower()
uppercase_name = clean_name.upper()

print("Original:", name)
print("Without Extra Spaces:", clean_name)
print("Lowercase:", lowercase_name)
print("Uppercase:", uppercase_name)

# ------------------------------------------

# Q6. Create a sentence containing the word "Python"
#     several times.
#
#     Use an appropriate string method to count how
#     many times "Python" appears.

sentence = "Python is easy. Python is powerful. I enjoy learning Python."

python_count = sentence.count("Python")

print("Number of times Python appears:", python_count)

# ------------------------------------------

# Q7. Create a sentence containing a specific word.
#
#     Use a string method to replace that word with
#     another word.
#
#     Print the original and modified sentences.

original_sentence = "I am learning Python."
modified_sentence = original_sentence.replace("Python", "Java")

print("Original Sentence:", original_sentence)
print("Modified Sentence:", modified_sentence)

# ==========================================

