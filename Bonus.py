# Bonus

wieght= input("your wieght: ")
height= input("your height: ")
wieght= float(wieght)
height= float(height)
bmi = wieght/(height*height)*10000
bmi= round(bmi,2)
print(f"Your BMI is {bmi}")



if bmi>=25:
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi>=18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")
    