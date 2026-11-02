weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))

if height > 0 and weight >= 0:
    bmi = weight / (height ** 2)
    print("BMI:", round(bmi, 2))
else:
    print("Enter valid weight and height")