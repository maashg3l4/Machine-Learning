def calculate_salary(basic, attendance):
    bonus = 0
    if attendance > 25:
        bonus = basic * 0.1
    total = basic + bonus
    return total

emp_name = 'Sohag'
salary = calculate_salary(30000, 26)
print(f'Employee: {emp_name}')
print(f'Final Salary with Bonus: {salary}')
