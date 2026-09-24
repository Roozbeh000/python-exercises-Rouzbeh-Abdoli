# Question 1

products={"Laptop": 1200, "phone": 800, "Tablet": 500, "Headphones": 50}

most_expensive= max(products, key=products.get)
print("Expensive prodect:", most_expensive)

cheapest= min(products, key=products.get)
print("Cheapest:", cheapest)

Average= sum(products.values()) / len(products)
print("Average:", Average)

expensive_products=[name for name, price in products.items() if price > 500]
print("500 more than other products:", expensive_products)

total= sum(products.values())
print("Total:", total)