# Question 03
total= 0
for i in range(1,11):
    if i % 2 != 0:
        i = i * 5
    else:
        i = i + 5
    total = total + i 
print(total)
