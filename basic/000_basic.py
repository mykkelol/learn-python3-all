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

# -----------------------------------------------------------------------------
# Question 7:
# Discuss range(start, end, step) and meaning of each argument with an example
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Question 8:
# Create Account class that can deposit, withdraw, transfer funds to another account, and record a transaction (type, amount, timestamp)
# Create Bank class that can get_top_k_accounts_by_outgoing, add, and get Account
# -----------------------------------------------------------------------------
from datetime import datetime

class Account:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def record_transaction(self, type, amount):
        self.transaction({
            'type': type,
            'amount': amount,
            'timestamp': datetime.now()
        })

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.record_transaction('deposit', amount)
            return True
        else:
            print('Amount cannot be 0')
        return False
    
    def withdraw(self, amount):
        if amount > 0:
            if amount >= self.balance:
                self.balance -= amount
                self.record_transaction('withdraw', amount)
                return True
            else:
                print('Insufficient funds')
        else:
            print('Amount cannot be 0')
        return False
    
    def transfer_funds(self, receiver, amount):
        if amount > 0:
            if amount >= self.balance:
                receiver.deposit(amount)
                print('Funds successfully transferred!')
                return True
            else:
                print('Insufficient funds')
        else:
            print('Amount cannot be 0')
        return False
    
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
    
    def get_account(self, account_number):
        return next((account for account in self.accounts if account.account_number == account_number), None)
    
    def get_top_k_accounts_by_outgoing(self, k):
        sorted_accounts = sorted(self.accounts, key=lambda account: sum(t['amount'] for t in account.transactions if t['type'] == 'withdraw'), reverse=True)
        return sorted_accounts[:k]
    
    def get_top_k_accounts_by_volume(self, k):
        sorted_accounts = sorted(self.accounts, key=lambda account: len(account.transactions), reverse=True)
        return sorted_accounts[:k]
    
# ************* Exercise 1: Basics *************

# Task 1: Create the `create_smile_armies` function that accepts a number of armies and a number of rows per army, returning armies of smilies.
def create_smile_armies(num_of_armies, num_of_rows):
    for j in range(num_of_armies):
        for i in range(num_of_rows):
            print('😀' * (i + 1))
            
create_smile_armies(3, 3)

# Task 2: Create the `intersection` function that accepts two lists and returns a list of their intersection.
def intersection(a, b):
    return [value for value in a if value in b]

print(intersection([1,2,3,4],[3,1,5,2,3]))

# ************* Exercise 2: List *************

# Task 1: Create the `lower_reversal` function that accepts a list of names, returning a list of it reversed and lowercase.
def lower_reversal(names):
    return [name.lower()[::-1] for name in names]

print(lower_reversal(['JOHN', 'Jane', 'JACK']))

# Task 2: Create the `get_n_matrix` function that accepts an N and returns an NxN matrix of stars.
def get_n_matrix(n):
    return [['*' * n for i in range(n)] for j in range(n)]

print(get_n_matrix(3))

# ************* Exercise 3: Dict, Tuple, Set *************

# Task 1: Create the `dict_it_up` function that accepts str1 and str2, returning two dicts.
def dict_it_up(str1, str2):
    return {str1[i]:str2[i] for i in range(len(str2))}
print(dict_it_up('abc', '123'))

# Task 2: Create the `do_it_all` function that accepts a list, converts it into a tuple, and returns a unique list.
def do_it_all(nums):
    return list(set(tuple(nums)))
print(do_it_all([1,2,3,4,4,3]))

# Task 3: Create the `multiple_letter_count` function that accepts a string and returns a dict that counts the number of occurrences of each letter.
def multiple_letter_count(string):
    return {c: string.count(c) for c in string}
print(multiple_letter_count('mississipi'))

# Task 4: Create the `check_palindrome` function that accepts a string and returns a boolean indicating if it's a palindrome.
def check_palindrome(string):
    return string == string[::-1]
print(check_palindrome('racecar'))

# Task 5: Create the `intersection_join` function that returns a list of intersections between two lists using join.
def intersection_join(a, b):
    return list(set(a) & set(b))
print(intersection_join([1,2,3],[2,3,4]))

# ************* Exercise 4: Lambda, *args, *kwargs *************

# Task 1: Create the `partition` function given a list of nums and a callback that validates each element.
def isEven(num):
    return num % 2 == 0
    
def partition(nums, callback):
    return [[n for n in nums if callback(n)], [n for n in nums if not callback(n)]]

print(partition([1,2,3,4,5], isEven))

# Task 2: Create the `all_my_friends` function to understand *args and **kwargs.
def all_my_friends(a, b, *numbers, word='woof', **words):
    return f'{a}, {b}, {numbers}, {word}, {words}'

print(all_my_friends('Elon', 'Jeff', 1,2,3,4, word='ruff',bob='purple'))

# Task 3: Create the `decrement_list` function that accepts a list of nums and returns a list with all elements decremented by 1.
def decrement_list(l):
    return [n - 1 for n in l]
print(decrement_list([1,2,3,4,5]))

# Task 4: Create the `is_all_strings` function that accepts a list and returns a boolean if the list contains all strings.
def is_all_strings(l):
    return all(type(s) == str for s in l)
print(is_all_strings(['s', 1]))
print(is_all_strings(['s', '1']))

# Task 5: Create the `get_longest_lyrics_songs` function that accepts a playlist and returns it sorted by longest lyrics.
def get_longest_lyrics_songs(l):
    return sorted(l, key=lambda song: len(song['lyric']),reverse=True)

# Task 6: Create the `max_magnitude` function that returns the max magnitude (furthest from zero) given a list.
def max_magnitude(l):
    return max(abs(n) for n in l)

# Task 7: Given three lists of student names, midterm grades, and final grades, create a function that returns a dict of students and their average grades.
def student_avg_grades(students, finals, midterms):
    list_approach = {student[0]: (student[1] + student[2])/ 2 for student in zip(students, finals, midterms)}

    lambda_approach = dict(
        zip(
            students,
            map(lambda pair: sum(pair) / len(pair), zip(finals, midterms))
        )
    )

    return lambda_approach

students = ['aang', 'korra', 'sato']
finals = [98, 89, 99]
midterms = [91, 95, 90]
print(student_avg_grades(students, finals, midterms))

# Task 8: Create the `interleave` function that returns one string interwoven from two provided strings.
def interleave(str1, str2):
    return ''.join(''.join(pair) for pair in zip(str1, str2))
print(interleave('spar','tan'))

# ************* Exercise 5: Debugging *************

# Task 1: Use pdb to debug the following function. Explain each line of code and identify any bugs.
def run_pdb():
    # Your code here
    pass

# Task 2: Create the `divide` function that handles division operations, including error handling for type errors and division by zero.
def divide(num1, num2):
    # Your code here
    pass

# ************* Exercise 6: OOP (Object-Oriented Programming) *************

# Task 1: Create a class `User` with specified attributes and methods.

# create class User that has class attributes, active_users and banned_users
# the class should have three instance attributes: username, likes, age
# the class should have three instance methods: logout, add_like, change_username
# the class should have one class method: from_csv
# the class should have three methods to access and write a private instance property: status
# the class should print the username and total likes
# create class Admin that inherits User with attributes (users_banned, active_admins) and methods (ban_user)
# the class Admin should leverage polymorphism when Admin logs out

# ************* Exercise 7: Iterators & Generators *************

# Task 1: Write a function that generates a Fibonacci sequence up to a given length.
def get_fib_list(n):
    pass

# Task 2: Write a generator function that generates a Fibonacci sequence up to a given integer.
def get_fib_generator(max):
    # Your code here
    pass

# Task 3: Write two functions to find a dict within a list using a generator expression and list comprehension. Compare performance.
def compare_generator_v_list(accounts, account_number):
    # Your code here
    pass

# ************* Exercise 8: Decorators *************

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

# ************* Exercise 10: File I/O *************

# Task 1: Create a function that updates users' names in a CSV file and returns the count of users updated.
def update_users_in_csv(name, new_name):
    # Your code here
    pass

# ************* Exercise 11: Regex *************

# Task 1: Create the `parse_date` function that accepts a DMY date string and returns a dict of the date components.
def parse_date(string):
    # Your code here
    pass

# ************* Exercise 12: SQLite3 *************

# Task 1: Write a function that queries a SQLite database to get books with a 5-star rating and a price less than $50.
def get_scraped_books():
    # Your code here
    pass

# ************* Exercise 13: String & Variables *************

# Task 1: Write a function that asks users for km input stored in kms var, then convert the km into miles stored in miles var, and rewrite miles but rounded. Then return the rounded miles with interopolation
def your_kms():
    pass

# ************* Exercise 14: List *************

# Task 1.1: Retrieve the last element using negative indexing
numbers = [10, 20, 30, 40, 50]
print()

# Task 1.2: Create a reversed version of numbers using slicing
print()

# Task 2.1: Join the fruits into a string separated by commas
fruits = ['apple', 'banana', 'cherry']
print()

# Task 2.2: Count how many times 4 appears in the list
numbers = [1, 2, 3, 4, 4, 4, 5]
print()

# Task 2.3: Replace 2, 3, 4 with 'a', 'b', 'c' using slicing
print()

# Task 2.4: Swap the elements in the list without using temporary variables
words = ['hello', 'world']
print()

# Task 3.1: Append 'green' to colors
colors = ['red', 'blue']
print()

# Task 3.2: Extend colors with ['yellow', 'purple']
print()

# Task 3.3: Insert 'orange' at the beginning of the colors list
print()

# Task 3.4: Remove 'blue' from the colors list
print()

# Task 3.5: Pop the last element from colors and print it
print()

# Task 4.1: Create a list of even numbers from nums using slicing
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

# Task 4.2: Reverse the nums list in-place
print()

# Task 4.3: Create a shallow copy of nums and prove it's a shallow copy
print()

# Task 4.4: Reverse the order of the first three elements in chars
print()

# Bonus: Explain the difference between list_a == list_a[:] and list_a is list_a[:]
# When slicing, i.e. list_a[:], Python creates a shallow copy of the initial list
# By creating a whole new list, Python saves this in a difference in the memory
# When comparing by == operator, we're checking if the elements in the list equals; thus, returns True
# When comparing by is keyword, we're checking if the two list are stored in the same place in the memory; thus, returns False

# ************* Exercise 15: List Comprehension *************

# Task 1: Return the first letter of each name in the list names
names = ["Elie", "Tim", "Matt"]
print()

# Task 2: Return all even numbers between 1 to 6
print()

# Task 3: Find the intersection between two lists (elements present in both lists)
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
print()

# Task 4: Reverse each name in the list names and convert them to lowercase
names = ["Elie", "Tim", "Matt"]
print()

# Task 5: Return a list of numbers between 1 and 100 that are divisible by 12
print()

# Task 6: Convert the string "amazing" to a list containing all its letters except for vowels
word = 'amazing'
print()

# Task 7: Print all coordinates from a list of location coordinates
locations = [[10.423, 9.123], [37.212, -14.092], [21.367, 32.572]]
print()

# Task 8: Return a 3x3 matrix filled with stars
print()

# Task 9: Return nested lists of [0, 1, 2] three times
print()

# ************* Exercise 16: Dictionary *************

# Exercise 1: Sum of Donations
# Given a dictionary of donations, calculate the total amount of donations.
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
print()

# Exercise 2: Initial Game State
# Set an initial state value of 0 for all game properties listed in the game_properties list.
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 
print()

# Exercise 3: Spotify Playlist Duration
# Given a playlist dictionary, calculate the total length of all songs in the playlist and update the playlist dictionary with this new key-value pair.
playlist = {
    'title': 'favorites', 
    'author': 'mykkelol', 
    'songs': [
        {
            'title': 'Malibu',
            'artists': ['Miley', 'DJ Khaled'],
            'duration': 2.5,
        },
        {
            'title': '22',
            'artists': ['Tay Tay', 'Mahomes'],
            'duration': 3,
        }
    ]
}
print()

# Exercise 4: String to Dictionary
# Given two strings, str1 and str2, create a dictionary with str1 characters as keys and str2 characters as corresponding values.
str1 = 'ABC'
str2 = '123'
print()

# Exercise 5: Odd or Even Dictionary
# Given a list of numbers, create a dictionary where the numbers are keys and the values indicate whether the number is odd or even.
nums = range(1,6)
print()

# Exercise 6: Update and Transform
# Given a dictionary of an instructor, update the key "color" and its value to uppercase.
my_dict = {'name': 'Blue', 'city': 'San Francisco', 'color': 'purple'}
print()

# Exercise 7: Lists to Dictionary Without Zip
# Given two lists, create a dictionary with list1 elements as keys and list2 elements as corresponding values without using the zip() function.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
print()

# Exercise 8: List of Lists to Dictionary
# Given a list of lists where each sublist contains two elements (a key and a value), convert this into a dictionary.
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]  
print()

# Exercise 9: Vowel Dictionary
# Create a dictionary with each vowel as a key and all values set to 0.
print()

# Exercise 10: ASCII Dictionary
# Create a dictionary where the keys are numbers from 65 to 90 (inclusive), and the values are the corresponding ASCII characters (capital A-Z).
print()

# ************* Exercise 17: Tuples & Sets *************

# Exercise 1: Creating and Accessing Tuples
print("Exercise 1: Creating and Accessing Tuples")
# 1. Create a tuple named `numbers` containing the numbers 1 through 4.
print()

# 2. Convert the list `[1, 3, 3, 7]` into a tuple named `list_to_tuple`.
list_to_tuple = tuple([1,3,3,7])
print()

# 3. Access and print the second element of the tuple `(1, 3, (3, 7))`.
complex_tuple = (1, 3, (3, 7))
print()

# 4. Create a tuple containing just the number 1 named `single_element_tuple`.
single_element_tuple = (1,)
print()

# Exercise 2: Tuple Methods
print("\nExercise 2: Tuple Methods")
values = (1, 3, 3, 7)

# 1. Count how many times `3` appears in the tuple `values`.
count_three = None
print("Number of 3s:", count_three)

# 2. Find the index of the number `7` in the tuple `values`.
index_seven = None
print("Index of 7:", index_seven)

# Sets Exercises

# Exercise 3: Working with Sets
print("\nExercise 3: Working with Sets")
# 1. Create a set and demonstrate adding a duplicate.
unique_numbers = None
unique_numbers
print("Unique Numbers Set:", unique_numbers)

# 2. Set comprehension to create squares from 0 to 9.
squares = None
print("Squares Set:", squares)

# 3. Count unique vowels in 'sequoia'.
unique_vowels_count = None
print("Unique Vowels Count in 'sequoia':", len(unique_vowels_count))

# Exercise 4: Advanced Set Operations
print("\nExercise 4: Advanced Set Operations")
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Add `6` to `set1`.
None
print("Set1 after adding 6:", set1)

# Remove `2` from `set1` using .remove() method.
None
print("Set1 after removing 2:", set1)

# Use .discard() method to remove `5` from `set2`.
None
print("Set2 after discarding 5:", set2)

# Union of `set1` and `set2`.
None
print("Union of Set1 and Set2:", union_set)

# Intersection of `set1` and `set2`.
None
print("Intersection of Set1 and Set2:", intersection_set)

# Demonstrate .copy() and .clear() methods.
sample_set = {1, 2, 3, 4, 5}
sample_set_copy = None
print("Copy of Sample Set:", sample_set_copy)
None
print("Sample Set after clearing:", sample_set)

# ************* Exercise 18: Functions *************
# Exercise 1: Return the Day of the Week
def return_day(n):
    pass
print(return_day(1))

# Exercise 2: Count Letter Occurrences
def multiple_letter_count(string):
    pass
print(multiple_letter_count('SAturday'))

# Exercise 3: Check if a String is a Palindrome
def check_palindrome(string):
    pass
print(check_palindrome('racecar'))

# Exercise 4: Product of All Even Numbers
def product_of_even(nums):
    pass
print(product_of_even([1,2,3,4,5]))

# Exercise 5: Capitalize a String
def capitalize_string(string):
    pass
print(capitalize_string('test'))

# Exercise 6: Filter Truthy Values
def compact(collection):
    pass
print(compact([0, 1, True, False, None, '', 'Test']))

# Exercise 7: Intersection of Two Lists
def intersection(collection1, collection2):
    pass
print(intersection([1,2,3,4],[2,4,6,8]))

# Exercise 8: Partition List Based on a Callback
def isEven(num):
    pass

def partition(nums, callback):
    pass

print(partition([1,2,3,4,5], isEven))

# Exercise 9: Understanding Function Parameters
def all_my_friends(a, b, *numbers, word='woof', **words):
    pass

# Call the function to demonstrate parameter usage
print(all_my_friends(1, 2, 3, beep=1, boop=2, bop=3))
print(all_my_friends(1, 2, 3, 4, 5, word='mewo', beep=1, boop=2, bop=3))

# Exercise 10: Advanced Calculator
def add(n1, n2):
    pass

def calculate(**kwargs):
    pass

print(calculate(operation=add, make_float=True, first=1, second=2))

# Demonstration of function calls
print(return_day(1))
print(multiple_letter_count("hello"))
print(check_palindrome("racecar"))
print(product_of_even([1, 2, 3, 4, 5, 6]))
print(capitalize_string("hello world"))
print(compact([0, 1, False, True, '', 'hello']))
print(intersection([1, 2, 3], [2, 3, 4]))
print(partition([1, 2, 3, 4, 5], isEven))
print(calculate(operation='add', make_float=True, first=1, second=2))

# ************* Exercise 19: Lambdas *************

# Exercise: Lambdas and Built-in Functions

# Decrement List
def decrement_list(l):
    pass

# Remove Negatives
def remove_negatives(l):
    pass

# Check if All Elements are Strings
def is_all_strings(lst):
    pass

# Sort Playlist by Length of Lyrics
playlist = [
    {'name': 'Talking to the moon', 'lyric': 'mooooooooo mooooooooon'},
    {'name': 'Malibu', 'lyric': 'ma bu'},
    {'name': 'Smooth criminal', 'lyric': 'mooooooooonwalking'},
]

def get_longest_lyrics_songs(playlist):
    pass

def get_longest_lyrics(playlist):
    pass

# Get Min and Max from a List
def get_extremes(l):
    pass

# Max Magnitude
def max_magnitude(l):
    pass

# Sum of Evens
def sum_of_evens(*args):
    pass

# Student Average Grades
students = ['aang', 'korra', 'sato']
finals = [98, 89, 99]
midterms = [91, 95, 90]

def student_avg_grades(students, finals, midterms):
    pass

# Interleave Strings
def interleave(str1, str2):
    pass

# Triple and Filter
def triple_and_filter(lst):
    pass

# Demonstration of function calls
print(decrement_list([1, 2, 3]))
print(remove_negatives([-1, 3, 4, -99]))
print(is_all_strings(['a', 'b', 'c']))
print(get_longest_lyrics_songs(playlist))
print(get_extremes([1, 2, 3, 4, 5]))
print(max_magnitude([-7, 22, 5, -99, 43]))
print(sum_of_evens(1, 2, 3, 4, 5, 6))
print(student_avg_grades(students, finals, midterms))
print(interleave('hi', 'ha'))
print(triple_and_filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]))

# ************* Exercise 20: Debugging and Error Handling *************

# Example of using pdb for debugging
first = 'First'
second = 'Second'
# import pdb; pdb.set_trace() # Uncomment to use pdb debugger
result = first + second  # This concatenates the strings 'First' and 'Second'
third = 'Third'  # This assigns the string 'Third' to the variable third
result += third  # This adds 'Third' to the result, making it 'FirstSecondThird'
print(result)  # Prints 'FirstSecondThird'

# Function to demonstrate error handling
def divide(num1, num2):
    try:
        return num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"

# Demonstrating the divide function with various inputs
print(divide(10, 2))  # Expected output: 5.0
print(divide(10, 'a'))  # Expected output: Please provide two integers or floats
print(divide(10, 0))  # Expected output: Please do not divide by zero

# Explanation of Common Errors and Handling
"""
- SyntaxError: This occurs when Python encounters incorrect syntax (e.g., missing colon, incorrect indentation).
- NameError: This error occurs when a variable is referenced before it has been assigned.
- TypeError: Happens when an operation is applied to an object of inappropriate type.
- IndexError: Occurs when trying to access an index that is out of range for a sequence.
- ValueError: This error is raised when a function receives an argument of correct type but inappropriate value.
- KeyError: Raised when a dictionary key is not found.
- AttributeError: Occurs when an attribute reference or assignment fails.

Using 'raise' to manually throw exceptions:
- 'raise' keyword is used to throw an exception if a condition occurs. The statement can be complemented with a custom error message.

Using try/except blocks for error handling:
- 'try' block lets you test a block of code for errors.
- 'except' block lets you handle the error.
- 'else' block executes if no errors were raised.
- 'finally' block executes regardless of the result of the try- and except blocks, and is often used for clean-up actions.
"""

# Note: The pdb.set_trace() command is commented out because it's meant for interactive debugging sessions.
# To use it, uncomment the import pdb; pdb.set_trace() line, and run the script in an environment where you can interact with the debugger.

# Realistic example of try, except, else, raise, and finally
def fetch_user_data(username):
    """
    Attempt to connect to database and fetch user data.
    Demonstrates try/except/else/finally blocks and custom exceptions.
    """
    db = DatabaseConnection(
        host="example.com",
        username="admin",
        password="wrong_password"  # Intentionally wrong to demonstrate error handling
    )
    
    try:
        print(f"Attempting to fetch data for user: {username}")
        db.connect()
        
        # Simulate data processing that might raise different types of errors
        if username == "":
            raise ValueError("Username cannot be empty")
        
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
            
        # If we get here, the connection was successful and username is valid
        print(f"Successfully retrieved data for {username}")
        
    except DatabaseConnectionError as e:
        print(f"Database connection failed: {e}")
        return None
        
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
        
    except TypeError as e:
        print(f"Type error: {e}")
        return None
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
        
    else:
        print("Data fetch completed successfully")
        return {"username": username, "status": "active"}
        
    finally:
        print("Cleanup: Ensuring database connection is closed")
        db.disconnect()

# ************* Exercise 21: Modules *************
# Modules in Python

# Function to check if arguments contain Python keywords
def contain_keywords(*args):
    from keyword import iskeyword
    return any(iskeyword(arg) for arg in args)

# Function to interleave two strings using a function from another module
def get_interwoven(str1, str2):
    # Assuming sect20_lambdas.py is in the same directory and contains the interleave function
    from sect20_lambdas import interleave
    return interleave(str1, str2)

# Function to print messages in ASCII art style using pyfiglet and termcolor
def print_art(message, color):
    # Note: You need to install pyfiglet and termcolor using pip before running this function
    # python3 -m pip install pyfiglet
    # python3 -m pip install termcolor
    from pyfiglet import Figlet
    from termcolor import colored

    try:
        ascii_art = Figlet(font='slant').renderText(message)
        colored_ascii = colored(ascii_art, color=color, on_color='on_green', attrs=['blink'])
        print(colored_ascii)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Check for Python keywords
    print(contain_keywords("def", "class", "foot"))  # Example output: True

    # Interleave two strings
    print(get_interwoven("hi", "ha"))  # Example output: "hhia"

    # Print ASCII art message
    # Commented out to prevent running on script execution; uncomment to use
    # message = input('Give me a message to print: ')
    # color = input('What is your favorite color? ')
    # print_art(message, color)

# This script demonstrates how to work with modules in Python, including importing and using functions from both built-in and external modules. 
# The `print_art` function requires the external modules `pyfiglet` and `termcolor` to be installed via pip.

# ************* Exercise 22: Dictionary *************
# Working with Dictionaries in Python

# Sum of all donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = None

# Setting initial game state
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
initial_game_state = {}.fromkeys(game_properties, 0)

# Creating a Spotify playlist
playlist = {
    'title': 'favorites',
    'author': 'mykkelol',
    'songs': [
        {'title': 'Malibu', 'artists': ['Miley', 'DJ Khaled'], 'duration': 2.5},
        {'title': '22', 'artists': ['Tay Tay', 'Mahomes'], 'duration': 3}
    ]
}

# Calculating total length of playlist
total_length = len(playlist['songs'])
pass

# Creating a dictionary from two strings
str1, str2 = 'ABC', '123'
my_dict = None

# Dictionary comprehension with conditionals
nums = range(1, 6)
nums_dict = None

# Updating a dictionary and converting specific keys/values to uppercase
instructor = {'name': 'Blue', 'city': 'San Francisco', 'color': 'purple'}

# Creating a dictionary from two lists without using zip()
list1, list2 = ["CA", "NJ", "RI"], ["California", "New Jersey", "Rhode Island"]

# Converting a list of lists into a dictionary
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# Creating a dictionary with vowels as keys and 0 as default value
vowel_dict = None

# Dictionary of ASCII values for capital letters A-Z
ascii_dict = None

# Demonstration of function calls and variable values
print("Total Donations:", total_donations)
print("Initial Game State:", initial_game_state)
print("Playlist with Total Duration:", playlist)
print("Dictionary from Strings:", my_dict)
print("Nums Dict (Odd/Even):", nums_dict)
print("Updated Instructor Dict:", updated_instructor)
print("State Dict:", state_dict)
print("Person Dict:", person_dict)
print("Vowel Dict:", vowel_dict)
print("ASCII Dict:", ascii_dict)