# Question 3
password = input("Enter your password:")
if len(password) == 8:
    if password[:4].isalpha() and password[-1].isdigit():
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
