# My first python program for GitHub contribution
print("Hello GitHub! I am starting my Python journey.")

# Simple calculation
a = 10
b = 20
print("The sum of a and b is:", a + b)


def welcome_msg(name):
    return f"Hello {name}, welcome to Day 3 of Python practice!"

print(welcome_msg("Sohag"))


numbers = [5, 10, 15, 20]
squared = [x**2 for x in numbers]
print(f"Original: {numbers}")
print(f"Squared: {squared}")