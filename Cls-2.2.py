# 3
letter = input("Enter a letter: ")
if letter.lower() in 'aeiou':
    print("It is a vowel")
else:
    print("It is a consonant")


# 4
number=int(input("Enter your number: "))
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")


    # 5
num_1=int(input("Enter 1st number: "))
num_2=int(input("Enter 2nd number: "))
if num_1>num_2:
    print("1st Number is greater")
elif num_2 > num_1:
    print("2nd Number is greater")
else:
    print("They are equal to each other")


    # 6
Score=int(input("Enter your score: "))
if Score>=90 and Score<=100:
    print("A")
elif Score>=80 and Score<=89:
    print("B")
elif Score>=70 and Score<=79:
    print("C")
elif Score>=60 and Score<= 69:
    print("D")
elif Score<60:
    print("F")


# 7
num=int(input("Enter the number: "))
if num>0:
    print("It is a positive number")
elif num<0:
    print("It is a negative number")
else:
    print("It is zero")



# 8

age=int(input("Enter your age: "))
cgpa=float(input("Enter your cgpa: "))
if age >=18 and age<=24 and cgpa>=3.00 and cgpa<3.50:
    print("You are eligible for this program")
elif  age >=18 and age<=24 and cgpa>=3.50:
    print("You are qualified for getting Priority for this program")
elif age>=24 and cgpa>=2.5 and cgpa<3.00:
    print("You are eligible")
else:
    print("yoy are not eligible")