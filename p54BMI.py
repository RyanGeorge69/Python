bmi=float(input("Enter your BMI(Body Mass Index)="))

if bmi<18.5:
    print("You are underweight")
elif bmi>=18.5 and bmi<24.9:
    print("Your weight is normal")
elif bmi>=25 and bmi<29.9:
    print("You are over weight")
elif bmi>=30:
    print("You are obese")