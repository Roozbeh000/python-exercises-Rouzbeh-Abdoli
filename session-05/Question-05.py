# Question 5

text= input("Enter a sentence:")
words = text.split()
longest= words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
        
print(longest)
print("Length:", len(longest))

