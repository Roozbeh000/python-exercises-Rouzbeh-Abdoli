# Question 7

Orders=[("Ali", "laptop"),("Sara", "Phone"),("Ali","Laptop"),("Sara","Laptop"),("Ali","Tablet"),("Reza","Phone")]
customer_orders={}
for customer, product in Orders:
    if customer not in customer_orders:
        customer_orders[customer]=[]
    customer_orders[customer].append(product)
    
print(customer_orders)

