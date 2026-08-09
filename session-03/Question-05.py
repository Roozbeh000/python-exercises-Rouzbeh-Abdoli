# Question 05

number1=float(input("Enter a number:"))
number2=float(input("Enter a number:"))
operator=input("Enter opertor such as: (+ - / *):")
if operator == '+':
    result= number1 + number2
elif operator == '-':
    result= number1 - number2
elif operator == '/':
    result= number1 / number2
elif operator == '*':
    result= number1 * number2
else:
    print("Invalid")
print(result)
