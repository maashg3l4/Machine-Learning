def safe_divide(a, b):
    try:
        result = a / b
        return f'Result: {result}'
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero!'
    except TypeError:
        return 'Error: Please provide numbers only!'

print(safe_divide(100, 5))
print(safe_divide(100, 0))
print(safe_divide(100, 'abc'))
