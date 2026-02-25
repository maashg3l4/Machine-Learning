def get_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 80: return 'A+'
    elif avg >= 70: return 'A'
    elif avg >= 60: return 'B'
    else: return 'Pass'

my_marks = [85, 78, 92, 65]
result = get_grade(my_marks)
print(f'Average Marks: {sum(my_marks)/len(my_marks)}')
print(f'Final Grade: {result}')
