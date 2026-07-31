# Question-06

price=int(input("Enter amount of money you've spent:"))
if price>1000000:
    final_price= price*0.85
elif price>=500000:
    final_price= price*0.90
else:
    final_price=price

print("Final price is:", final_price)

