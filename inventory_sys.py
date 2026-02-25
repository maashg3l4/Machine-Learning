stock = {'Laptop': 10, 'Mouse': 3, 'Keyboard': 15, 'Monitor': 2}
low_stock = []
for item, count in stock.items():
    if count < 5:
        low_stock.append(item)

print('--- Inventory Report ---')
print(f'Current Stock: {stock}')
print(f'Items to Restock: {low_stock}')
