names = ['Sohag Miah', 'Masud Rana', 'Karim Uddin']
company = 'techcorp.com'
emails = []

for name in names:
    clean_name = name.lower().replace(' ', '.')
    email = f'{clean_name}@{company}'
    emails.append(email)

print('Generated Emails:')
for e in emails:
    print(f'- {e}')
