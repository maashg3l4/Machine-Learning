import time
print('Starting Process...')
for i in range(1, 6):
    print(f'Processing Step {i} [', '#' * i, ' ' * (5-i), ']')
    time.sleep(0.5)
print('Process Completed Successfully!')
