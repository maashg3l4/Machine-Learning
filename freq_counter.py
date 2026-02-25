numbers = [1, 2, 2, 3, 4, 4, 4, 5]
frequency = {}
for n in numbers:
    frequency[n] = frequency.get(n, 0) + 1

print('Number Frequency Map:')
for num, count in frequency.items():
    print(f'Number {num} appears {count} times')
