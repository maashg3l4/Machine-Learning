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


users = {"admin": "active", "sohag": "active", "guest": "inactive"}
active_only = {name: status for name, status in users.items() if status == "active"}
print("Active Users:", active_only)



try:
    val = int("123a")
except ValueError as e:
    print(f"Caught an error: {e}")
finally:
    print("Execution complete.")


# basic_python.py - Phase 5
def calculate_summary(data):
    return {"Total Sum": sum(data), "Max": max(data), "Min": min(data)}

my_data = [45, 12, 89, 3, 27]
print("Data Summary:", calculate_summary(my_data))