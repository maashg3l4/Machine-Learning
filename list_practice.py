# Working with Lists
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Mango")
print("My fruit list:", fruits)
print("First fruit:", fruits[0])

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# Prothom 3-ti element
print("First three:", numbers[:3])
# Majhkhaner kichu element
print("Middle part:", numbers[3:7])
# Shesh dik theke
print("Last two:", numbers[-2:])

cars = ["Toyota", "BMW", "Audi", "Tesla"]
# Alphabetically sajano
cars.sort()
print("Sorted cars:", cars)
# Ulto bhabe sajano
cars.reverse()
print("Reversed list:", cars)