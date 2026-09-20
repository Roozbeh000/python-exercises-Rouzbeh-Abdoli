# Question 9

connect_username="admin"
connect_password="1234"
for attempt in range(3):
    username=input("Eusername:")
    password=input("Password:")
    
    if username == connect_username and password == connect_password:
        print("Login successful")
        break
    else:
        print("Wrong username or password")
        print("Attempts remaning:", 2 - attempt)