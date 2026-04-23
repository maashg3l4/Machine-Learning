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

# Topic: Basic Variables in Python
# Purpose: Storing simple data for ML models

# String: Storing model or dataset name
dataset_name = "California Housing Data"
model_type = "Regression"

# Integer: Storing counts
features_count = 8
iterations = 1000

# Float: Storing precision values
learning_rate = 0.001
threshold = 0.5

# Boolean: Flags for model state
is_model_trained = False
shuffle_data = True

print(f"Dataset: {dataset_name} | Features: {features_count}")
print(f"Is Trained: {is_model_trained}")

# Topic: Data Type Identification
# Purpose: Knowing the data format before processing

val_int = 100
val_float = 99.9
val_str = "Neural Network"
val_bool = True

# Checking and printing types
print(f"Type of {val_int}: {type(val_int)}")
print(f"Type of {val_float}: {type(val_float)}")
print(f"Type of '{val_str}': {type(val_str)}")
print(f"Type of {val_bool}: {type(val_bool)}")

# Simple math with variables
a = 10
b = 5
print(f"Sum of {a} and {b} is: {a + b}")

# Topic: Type Casting / Conversion
# Purpose: Converting raw data strings into numbers

# String to Integer
raw_input = "250"
processed_input = int(raw_input)

# Integer to Float
base_accuracy = 92
final_accuracy = float(base_accuracy) / 100

# Converting to String for messages
version = 3.8
version_msg = "Python Version: " + str(version)

print(f"Processed Input: {processed_input} (Type: {type(processed_input)})")
print(f"Final Accuracy: {final_accuracy}")
print(version_msg)