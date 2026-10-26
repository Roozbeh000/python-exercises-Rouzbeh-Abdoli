# Question 2

def process_order(customer, *products, **options):
    discount= options.get("discount", 0)
    tax= options.get("tax", 0)
    shipping= options.get("shipping", 0)
    
    total=len(products) * 1000000
    total = total - (total * discount / 100)
    total = total + (total * tax / 100)
    total = total + shipping 
    
    order = {
        "customer": customer,
        "products": list(products),
        "discount": discount,
        "tax": tax,
        "shipping": shipping,
        "final_price": total
    }
    
    return order

result = process_order(
    "Ali",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=10,
    tax=9,
    shipping=200000
)

print(result)