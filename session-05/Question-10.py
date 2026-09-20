# Question 10

sentence1= input("Sentence 1:")
sentence2= input("Sentence 2:")

word1= sentence1.split()
word2= sentence2.split()

print("Common words:")

for word in word1:
    if word in word2:
        print(word)

