# Question 07

color1=input("Enter a color:")
color2=input("Enter a color:")
color3=input("Enter a color:")
if color1 == color2 and color2 == color3:
    print("All of them areEqual")
elif color1 == color2:
    print("color1 and color2 are Equal.")
elif color1 == color3:
    print("color1 and color3 are Equal.")
elif color2 == color3:
    print("color2 and color3 are Equal.")
else:
    print("None of them are Equal.")