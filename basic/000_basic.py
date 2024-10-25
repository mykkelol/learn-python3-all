# ==============================================================================
# Quiz on Python Logical Operators and Comparators
# ==============================================================================

# -----------------------------------------------------------------------------
# Question 1:
# Describe the 'not' logical operator in Python. How does it work, and provide
# examples.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question 2:
# Explain the difference between 'is' and '=='. Include examples in your explanation.
# -----------------------------------------------------------------------------

# ==============================================================================
# Quiz on Operators, Variables, and Strings in Python
# ==============================================================================

# -----------------------------------------------------------------------------
# Question 1:
# Explain the operation and use cases of the following operators: **, %, //, *, /, -, +.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question 2:
# Describe dynamic typing in Python and provide an example.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question 3:
# What are Dunder variables in Python? Give an example.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question 4:
# Explain the significance of the "None" value in Python.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question 5:
# Describe string interpolation in Python and provide an example using the 'f' string.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question 6:
# How does Python handle negative string indexes?
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question 7:
# Discuss data type conversion in Python with examples for int(), float(), and str() functions.
# -----------------------------------------------------------------------------

# Exercise 1: Basics

# Task 1: Create the `create_smile_armies` function that accepts a number of armies and a number of rows per army, returning armies of smilies.
def create_smile_armies(num_of_armies, num_of_rows):
    # Your code here
    pass

# Task 2: Create the `intersection` function that accepts two lists and returns a list of their intersection.
def intersection(a, b):
    # Your code here
    pass

# Exercise 2: List

# Task 1: Create the `lower_reversal` function that accepts a list of names, returning a list of it reversed and lowercase.
def lower_reversal(names):
    # Your code here
    pass

# Task 2: Create the `get_n_matrix` function that accepts an N and returns an NxN matrix of stars.
def get_n_matrix(N):
    # Your code here
    pass

# Exercise 3: Dict, Tuple, Set

# Task 1: Create the `dict_it_up` function that accepts str1 and str2, returning two dicts.
def dict_it_up(str1, str2):
    # Your code here
    pass

# Task 2: Create the `do_it_all` function that accepts a list, converts it into a tuple, and returns a unique list.
def do_it_all(nums):
    # Your code here
    pass

# Task 3: Create the `multiple_letter_count` function that accepts a string and returns a dict that counts the number of occurrences of each letter.
def multiple_letter_count(string):
    # Your code here
    pass

# Task 4: Create the `check_palindrome` function that accepts a string and returns a boolean indicating if it's a palindrome.
def check_palindrome(string):
    # Your code here
    pass

# Task 5: Create the `intersection_join` function that returns a list of intersections between two lists using join.
def intersection_join(a, b):
    # Your code here
    pass

# Exercise 4: Lambda, *args, *kwargs

# Task 1: Create the `partition` function given a list of nums and a callback that validates each element.
def partition(nums, callback):
    # Your code here
    pass

# Task 2: Create the `all_my_friends` function to understand *args and **kwargs.
def all_my_friends(a, b, *numbers, word='woof', **words):
    # Your code here
    pass

# Task 3: Create the `decrement_list` function that accepts a list of nums and returns a list with all elements decremented by 1.
def decrement_list(l):
    # Your code here
    pass

# Task 4: Create the `is_all_strings` function that accepts a list and returns a boolean if the list contains all strings.
def is_all_strings(l):
    # Your code here
    pass

# Task 5: Create the `get_longest_lyrics_songs` function that accepts a playlist and returns it sorted by longest lyrics.
def get_longest_lyrics_songs(l):
    # Your code here
    pass

# Task 6: Create the `max_magnitude` function that returns the max magnitude (furthest from zero) given a list.
def max_magnitude(l):
    # Your code here
    pass

# Task 7: Given three lists of student names, midterm grades, and final grades, create a function that returns a dict of students and their average grades.
def student_avg_grades(students, finals, midterms):
    # Your code here
    pass

# Task 8: Create the `interleave` function that returns one string interwoven from two provided strings.
def interleave(str1, str2):
    # Your code here
    pass

# Exercise 5: Debugging

# Task 1: Use pdb to debug the following function. Explain each line of code and identify any bugs.
def run_pdb():
    # Your code here
    pass

# Task 2: Create the `divide` function that handles division operations, including error handling for type errors and division by zero.
def divide(num1, num2):
    # Your code here
    pass

# Exercise 6: OOP (Object-Oriented Programming)

# Task 1: Create a class `User` with specified attributes and methods.
class User:
    # Your code here
    pass

# Task 2: Create a subclass `Admin` that inherits from `User` and includes additional attributes and methods.
class Admin(User):
    # Your code here
    pass

# Exercise 7: Iterators & Generators

# Task 1: Write a function that generates a Fibonacci sequence up to a given length.
def get_fib_list(n):
    # Your code here
    pass

# Task 2: Write a generator function that generates a Fibonacci sequence up to a given integer.
def get_fib_generator(max):
    # Your code here
    pass

# Task 3: Write two functions to find a dict within a list using a generator expression and list comprehension. Compare performance.
def compare_generator_v_list(accounts, account_number):
    # Your code here
    pass

# Exercise 8: Decorators

# Task 1: Create functions `add` and `multiply` that use a decorator to log and document their execution.
def log_function_executions(fn):
    # Your decorator code here
    pass

def add(n1, n2):
    # Your function code here
    pass

def multiply(n1, n2):
    # Your function code here
    pass

# Exercise 10: File I/O

# Task 1: Create a function that updates users' names in a CSV file and returns the count of users updated.
def update_users_in_csv(name, new_name):
    # Your code here
    pass

# Exercise 11: Regex

# Task 1: Create the `parse_date` function that accepts a DMY date string and returns a dict of the date components.
def parse_date(string):
    # Your code here
    pass

# Exercise 12: SQLite3

# Task 1: Write a function that queries a SQLite database to get books with a 5-star rating and a price less than $50.
def get_scraped_books():
    # Your code here
    pass