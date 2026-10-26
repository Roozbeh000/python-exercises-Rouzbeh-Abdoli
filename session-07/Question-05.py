# Question 5

logs=[("Ali", "LOGIN", 200),
      ("Ali", "DOWNLOAD", 200)
      ("Sara", "LOGIN", 403)
      ("Reza", "LOGIN", 200)
      ("Sara", "LOGIN", 403)
      ("Sara", "LOGIN", 403)
]

def ananlyze_login(logs):
   check=[]
   logins=0
   failed_logins=0
   operations={}
   
   for i in logs:
       user=i[0]
       action=i[1]
       code=i[2]
       
       if user not in operations:
           operations[user]= 0
       operations[user] += 1
       
       if action == "LOGIN" and code == 200:
           logins += 1
       if action == "LOGIN" and code == 403:
           failed_logins += 1
       if user not in check:
           counter = 0
           
           for y in logs:
               if y[0] == user and y[1] == 'LOGIN' and y[2] == 403:
                   counter += 1
           if counter >= 3:
                print(user, "is suspicious")
                   
           check.append(user)
    
    print("Successful logins:", logins)
    print("Failed logins:", failed_logins)
    print("User operations:", operations)

ananlyze_login(logs)