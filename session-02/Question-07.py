credit_number=input("Enter your credit card number:")
if len(credit_number) !=16:
    print("The credit card number you've written needs to be 16 digits !")
else: 
    cn=credit_number[0:4]
if cn == "6219":
    print("Bank: Blu")
elif cn == "6037":
    print("Bank: Mellat")
elif cn == "6274":
    print("Bank: Tejarat")
else:
    print("Unkown bank")


