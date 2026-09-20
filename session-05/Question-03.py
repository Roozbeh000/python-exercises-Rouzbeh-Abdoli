# Question 3

text= input("Enter a text:")
letters=0
uppercase=0
lowercase=0
digits=0
spaces=0
special=0

for char in text:
    if char.isalpha():
        letters += 1
        
        if char.isupper():
            uppercase += 1
        else:
            lowercase += 1
        
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special += 1
print("letters:", letters)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
