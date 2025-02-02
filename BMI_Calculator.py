#Code below this line

weight = float(input("What is your weight? "))
height = float(input("What is your height? "))
kg = 0.453
height_m = 0.0254
bmi = (weight * kg / ((height*height_m)**2))

print(bmi)