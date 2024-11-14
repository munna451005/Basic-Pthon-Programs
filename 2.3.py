age=int(input("Enter your age: "))
cgpa=float(input("Enter your cgpa: "))
if age >=18 and age<=24 and cgpa>=3.00 and cgpa<3.50:
    print("You are eligible for this program")
elif  age >=18 and age<=24 and cgpa>=3.50:
    print("Congratulations, you are qualified for getting Priority for this program")
elif age>24 and cgpa>=2.5 :
    print("You are eligible")
else:
    print("Sorry, You are not eligible")