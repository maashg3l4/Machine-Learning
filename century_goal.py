import random
print('--- Welcome to the Century Club ---')
target = 100
current = random.randint(90, 100)
if current >= target:
    print(f'Score: {current}. Congrats! You hit the century!')
else:
    print(f'Score: {current}. Almost there!')
print('GitHub Contributions: Goal Reached ✅')
