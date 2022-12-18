x = int(input("enter x:"))
y = int(input("enter y:"))
if x > 0 and y > 0:
    print("1st")
elif x < 0 and y > 0:
    print("2nd")
elif x < 0 and y < 0:
    print("3rd")
elif x > 0 and y < 0:
    print("4th")
else:
    print("error")