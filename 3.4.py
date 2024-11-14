# conditional

score=int(input("Enter your score: "))

if score>=80 and score<=100:
    print("A+")
elif score>=60 and score<=79:
    print("B+")
elif score>=0 and score<=59:
    print("F")

# loop
score=[56,99,100,50,70,67]
for x in score:
    if x >= 80 and x <= 100:
          print("A+")
    elif x >= 60 and x <= 79:
           print("B+")
    else :
           print("F")
