a_x = int(input("enter point A axis X coordinate:"))
a_y = int(input("enter point A axis Y coordinate:"))
b_x = int(input("enter point B axis X coordinate:"))
b_y = int(input("enter point B axis Y coordinate:"))
distance = ((b_x-a_x)**2 + (b_y-a_y)**2)**0.5
print(distance)