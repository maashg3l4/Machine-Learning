students = ['Sohag', 'Masud', 'Karim']
new_student = 'Jashim'
if new_student not in students:
    students.append(new_student)
    print(f'Added {new_student}. New List: {students}')
else:
    print('Student already exists!')
for i, name in enumerate(students, 1):
    print(f'ID {i}: {name}')
