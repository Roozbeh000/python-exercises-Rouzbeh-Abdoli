# Question 2

Inventory={"Apple": 20, "Banana": 5, "Orange": 0, "Milk": 12, "bread": 0}
availabe=[]
out_of_stock=[]

for product, count in Inventory.items():
    if count > 0:
        availabe.append(product)
    else:
        out_of_stock.append(product)
        
print("Available:")
for product in availabe:
    print(product)
    
print("Out of stock:")
for product in out_of_stock:
    print(product)
        
