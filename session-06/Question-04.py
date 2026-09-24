# Question 4

Employees={"Ali": 3000, "Sara": 4500, "Reza": 2800}

print(max(Employees, key=Employees.get), max(Employees.values()))

print(sum(Employees.values()) / len(Employees))

for name in Employees:
    if Employees[name] > 3000:
        print(name)
print(min(Employees, key=Employees.get))
