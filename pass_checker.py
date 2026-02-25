def check_password(password):
    if len(password) < 8:
        return 'Weak: Too short!'
    if password.isalpha() or password.isdigit():
        return 'Medium: Mix letters and numbers.'
    return 'Strong: Perfect!'

print('Pass123:', check_password('Pass123'))
print('Sohag2026!:', check_password('Sohag2026!'))
