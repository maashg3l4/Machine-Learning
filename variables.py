name = "ML Learner"  # String
age = 25             # Integer
accuracy = 98.5      # Float
is_trained = True    # Boolean

print(f"{name} is learning at {accuracy}% speed.")

features = ["size", "color", "weight"]
target = {"label": "Apple", "confidence": 0.95}
features.append("texture")

print(features[0])  # Accessing first element
print(target["label"]) # Accessing dict value

scores = [85, 92, 78, 95, 88]
passed_scores = []

for s in scores:
    if s > 90:
        print(f"Excellent score: {s}")
    elif s > 80:
        passed_scores.append(s)

print(f"Passed: {passed_scores}")



def calculate_error(actual, predicted):
    return abs(actual - predicted)


square = lambda x: x ** 2

print(calculate_error(10, 8.5))
print(square(4))


numbers = [1, 2, 3, 4, 5]

squares = [n**2 for n in numbers]

print(squares) # Output: [1, 4, 9, 16, 25]




student_data = {
    "id": 101,
    "name": "Sohag",
    "skills": ["Python", "Git", "Django"],
    "is_active": True
}


student_data["current_goal"] = "Machine Learning"

print("Keys in dictionary:", student_data.keys())
print("Student Skills:", student_data["skills"])

# Topic: Arithmetic Operations with Variables
# Purpose: Calculating loss or distance in ML

x = 15
y = 4

# Basic Math
sum_res = x + y       # Jog
sub_res = x - y       # Biyog
mul_res = x * y       # Gun
div_res = x / y       # Vag (Result float hobe)
floor_div = x // y    # Vag (Result purno sonkhya hobe)
mod_res = x % y       # Vagshesh (Reminder)
exp_res = x ** 2      # Power (Square kora)

print(f"Sum: {sum_res}, Power: {exp_res}")
print(f"Float Div: {div_res}, Floor Div: {floor_div}")

# Topic: String Methods
# Purpose: Cleaning Text Data

raw_text = "  Machine Learning is AWESOME!  "

# Cleaning whitespace
clean_text = raw_text.strip()

# Changing cases
lower_text = clean_text.lower()
upper_text = clean_text.upper()

# Replacing words
new_text = clean_text.replace("AWESOME", "Powerful")

print(f"Original: '{raw_text}'")
print(f"Clean & Lower: '{lower_text}'")
print(f"Replaced: '{new_text}'")


# Topic: Comparison and Logic
# Purpose: Model validation logic

accuracy = 0.85
threshold = 0.80

# Comparison Operators
is_better = accuracy > threshold  # True
is_equal = accuracy == 1.0        # False

# Logical Operators (AND, OR, NOT)
has_data = True
is_trained = False

# Jodi data thake kintu train na hoy
can_start_training = has_data and (not is_trained)

print(f"Is accuracy better than threshold? {is_better}")
print(f"Can we start training? {can_start_training}")