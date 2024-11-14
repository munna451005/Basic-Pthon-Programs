#pracice-2
age=5
print(age)

#practice-2
number_one=5
number_two=10
sum=number_one+number_two
print(sum)

import math
number_two=10.7
print(math.ceil(number_two))

number=5
result=math.factorial(number)
print(result)

number=5
result=math.pow(2,3)
print(result)
import math
#celi
import math
num=5.2
result=math.ceil(num)
print(result)


#floor
import math
num=5.8
result=math.floor(num)
print(result)
#abs
num= -5.2
result=abs(num)
print(result)

#factorial
import math
num=5
result=math.factorial(num)
print(result)

#pow
import math
result=math.pow(2,3)
print(result)

print(math.pi)


result=math.gcd(56,98)
print(result)

result=math.lcm(10,5)
print(result)

result=math.sqrt(36)
print(result)


# string

multiline_string="""something 
here 
there gone"""

num=6
print(multiline_string)
print(multiline_string.upper())
print(multiline_string.title())
print(multiline_string.find("t"))
print(multiline_string.replace("s","S"))
# new
print(multiline_string.lower())
print((multiline_string.count("something")))


course_Name="Python"
print(f"My course name is {course_Name}")


num1=input('enter 1st number:')
num2=input('enter 2nd number:')
sum=int(num1)+int(num2)
print(f'the sum of{num1} and {num2} is {sum}')


your_name=input("your name is: ")
print(f"your name is{your_name}")


password=2017
new=input("your password: ")
if password==int(new):
    print("Access granted")
else:
    print("Access denied")