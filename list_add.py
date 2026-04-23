# Topic: Python Lists (The Dataset Basics)
ml_libraries = ["NumPy", "Pandas", "Scikit-Learn"]
print(f"Total Libraries: {len(ml_libraries)}")

# Adding new item
ml_libraries.append("TensorFlow")
print(f"Updated List: {ml_libraries}")

# Slicing (ML-e data split korar jonno lage)
first_two = ml_libraries[:2]
print(f"First two: {first_two}")

# Topic: List Math & Sorting
scores = [88, 92, 75, 99, 82]

# Math operations on lists
max_score = max(scores)
min_score = min(scores)
avg_score = sum(scores) / len(scores)

print(f"Max Accuracy: {max_score}, Min: {min_score}, Avg: {avg_score}")

# Sorting data
scores.sort(reverse=True)
print(f"Ranked Scores: {scores}")

