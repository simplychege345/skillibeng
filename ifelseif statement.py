marks=int(input("enter marks:"))
if marks >=80 and marks <=100:
    print("you have an A")
elif marks>=60 and marks<=79:
    print("you have a B")
elif marks>=40 and marks<=59:
    print("you have a C")
elif marks>=0 and marks<=39:
    print("failed")
else:
    print("wrong input")