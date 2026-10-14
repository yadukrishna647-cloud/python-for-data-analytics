age = int(input("Enter your age: "))
if age < 5:
    print("free")
elif age >= 5 and age <= 12:
    print("child ticket")
elif age >= 13 and age <= 59:
    print("adult ticket")
else:
    print("senior citizen ticket")    