cart = [
    {'item': 'Phone', 'price': 20000},
    {'item': 'Cover', 'price': 500},
    {'item': 'Charger', 'price': 1200}
]
subtotal = sum(item['price'] for item in cart)
tax = subtotal * 0.05
total = subtotal + tax

print(f'Subtotal: {subtotal} BDT')
print(f'Tax (5%): {tax} BDT')
print(f'Grand Total: {total} BDT')
