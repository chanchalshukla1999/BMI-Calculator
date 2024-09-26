def Bmi_calculation(weight,height):
    height_in_meters = height/100
    BMI = weight/(height_in_meters **2)
    return BMI
def bmi_category(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25.0:
        return "Normal Weight"
    elif 25.0 <= BMI < 30.0:
        return "Overweight"
    else:
        return "Obesity"
    

weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter you height in centimeter:"))

calculation = Bmi_calculation(48,60)
category = bmi_category(calculation)

print(f"YOUR BMI IS: {calculation:.2f} AND YOUR ARE IN THIS CATEGORY: {category}")


