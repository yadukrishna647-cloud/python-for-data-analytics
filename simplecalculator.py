no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    result = no1 + no2
elif opertor == "-":
    result = no1 - no2
elif operator == "*":
    result = no1 * no2
elif operator == "/":
    if no2 != 0:
        result = no1 / no2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"
print("Result:", result)