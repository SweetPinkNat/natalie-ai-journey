# Simple function, no parameters
def welcome():
    print("Welcome to your Python journey!")

welcome()

# Function with a parameter
def greet(name):
    print(f"Hey there, {name}!")

greet("Natalie")
greet("Damien")

# Function with a return value
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print(result)

# Function using multiple parameters and math
def calculate_area(width, height):
    return width * height

area = calculate_area(4, 6)
print(f"The area is {area}")