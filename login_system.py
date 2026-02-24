users = {'admin': '1234', 'sohag': 'pass56'}
username = 'sohag'
password = 'pass56'

if username in users:
    if users[username] == password:
        print('Access Granted! Welcome', username)
    else:
        print('Wrong Password!')
else:
    print('User Not Found!')
