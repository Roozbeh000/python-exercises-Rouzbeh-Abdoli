# Question 6

text=input("Enter a text:")
keywords=["hack", "fraud", "scam", "password"]

words= text.split()
for word in keywords:
    count= words.count(word)
    
if count > 0:
    print(word, "=", count)