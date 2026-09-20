# Question 2

text= input("Enter a word:")
result= ""
for char in text:
    if char not in result:
        result += char
print(result)
