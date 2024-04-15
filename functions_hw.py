#  The Calculator App

# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y
    
def calculator():
    while True:
        try:
            user_input = input("Enter an expression (ex., 'num1 + num2'): ")
            if user_input == 'done':
                break
            num1, op, num2 = user_input.split()
            num1 = float(num1)
            num2 = float(num2)
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                result = "Invalid operation"
            print("Result:", result)
        except ValueError:
            if user_input != 'done':
                print("Please enter a valid expression.")
calculator()        

            

# def user_input():
#     while True:
#         try:
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("Enter the second number: "))
#             return num1, num2
#         except ValueError:
#             print("Please enter valid numbers.")
# user_input()

# def calculator():
#     num1, num2 = user_input()
    # print(add(num1, num2))
    # print(subtract(num1, num2))
    # print(multiply(num1, num2))
    # print(divide(num1, num2))

print("=============================================================")

# The Shopping List Maker

# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

shopping_list = []

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")
def view_list():
    print(shopping_list)

add_item(shopping_list, 'glasses')
add_item(shopping_list, "pants")
view_list()
remove_item(shopping_list, 'glasses')
view_list()

print("=====================================================================")

# The Grade Analyzer

# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
# Task 2: Implement a function to find the highest and lowest grade.
# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
"""
    Function to calculate the average grade.
    Args:
    - grades: a list of numerical grades
    Returns:
    - average_grade: the average grade
    """

grades = [88, 96, 79, 91, 74]

def average_grade(grades):

    total = sum(grades)
    average_grade = total / len(grades)
    return average_grade

average_grade(grades)

def highest_and_lowest_grade(grades):

    highest_grade = max(grades)
    lowest_grade = min(grades)
    return highest_grade, lowest_grade

highest_and_lowest_grade(grades)

def grading(grades):
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    return letter_grades

grading(grades)

print("Average grade:", average_grade(grades))
print("Highest grade:", highest_and_lowest_grade(grades)[0])
print("Lowest grade:", highest_and_lowest_grade(grades)[1])
print("Letter grades:", grading(grades))

my_list = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(my_list):
    print(f"Index {index}: {fruit}")