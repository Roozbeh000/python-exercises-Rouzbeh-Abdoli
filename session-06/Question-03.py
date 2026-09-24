# Question 3

word=input("Enter a word:")
characters={}
for char in word:
    if char.isalpha():
        if char in characters:
            characters[char]+=1
        else:
            characters[char]=1
print(characters)