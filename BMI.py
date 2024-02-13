weight =float(input("Enter weight in kg"))
height =float(input("Enter your height in metres"))
bmi = weight /(height**2)

if bmi < 18.5:
    category= "under weight"
elif 18.5 <= bmi < 25 :
    category="Normal"
elif 25 <= bmi <29.9 :
    category="overweight"
else:
    category="obese"
print (f"your bmi is {bmi:2f}and your classif")