unit = int(input("Enter the number of units consumed: "))
if unit <= 100:
    total = unit *2
elif unit <= 200:
    total = 100 * 2 + (unit - 100) * 3
elif unit <= 400:
    total = 100 * 2 + 100 * 3 + (unit - 200) * 5
else:
    total = 100 * 2 + 100 * 3 + 200 * 5 + (unit - 400) * 7
print("total amount:",total) 