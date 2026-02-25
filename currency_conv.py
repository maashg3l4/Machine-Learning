rates = {'USD': 110, 'EUR': 120, 'INR': 1.3}
amount_bdt = 5000
conversions = {curr: amount_bdt / rate for curr, rate in rates.items()}

print('--- Currency Conversion from 5000 BDT ---')
for curr, val in conversions.items():
    print(f'{curr}: {val:.2f}')
