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


