text = "  Python is Amazing!  "
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Trimmed:", text.strip()) 
print("Replace:", text.replace("Amazing", "Powerful"))

about_ml = """Machine Learning is a subset of AI.
It focuses on teaching computers to learn from data."""
print(about_ml)
print("Total characters:", len(about_ml))
print("Is 'AI' present?", "AI" in about_ml)

def welcome_user(user_name):
    return f"Hello {user_name}, welcome to your ML journey!"

message = welcome_user("Sohag")
print(message)

def calculate_area(length, width):
    return length * width

result = calculate_area(5, 10)
print("Area of the rectangle:", result)

