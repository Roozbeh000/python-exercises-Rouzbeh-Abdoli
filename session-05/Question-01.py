# Question 1

password= input("Enter your password:")
if len(password) < 8:
    print("password must contain a least 8 characters")
if not any(c.isupper() for c in password):
    print("password must contain an upper case letter.")
if not any(c.islower() for c in password):
    print("password must contain an lower case letter.")
if not any(c.isdigit() for c in password):
    print("password must contain a number.")
if not any(c in "%$#@" for c in password):
    print("passworrd must contain an special letter.")
if (len(password) >= 8
    and any(c.isupper() for c in password)
    and any(c.islower() for c in password)
    and any(c.isdigit() for c in password)
    and any(c in "%$#@" for c in password)):
    print("password is valid")
