temp = 32
unit = 'Celsius'
print(f'Current Temperature: {temp}{unit}')

if temp > 30:
    advice = 'It is hot! Stay hydrated.'
elif temp >= 20:
    advice = 'Weather is pleasant.'
else:
    advice = 'It is cold! Wear a jacket.'

print('Advice:', advice)
