height_m = float(input("Enter your Height in meter :- "))
weight_kg = float(input("Enter your Weight in Kg :- "))

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    else:
        category = "Overweight"
    return bmi, category


bmi, category = calculate_bmi(weight_kg, height_m)
print(f"Your BMI: {bmi:.1f} - {category}")
