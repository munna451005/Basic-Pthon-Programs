from traceback import print_tb

x=12
counter=0
while counter<x:
    counter=counter+1
    print(counter)


x=12
counter=0
while range(10):
    if counter>5:
        break
    counter=counter+1
    print(counter)



number=[2,14,54,24,64,100,15,144]
user_number=int(input("enter your number"))

for x in number:
    if x== user_number:
        print("number found")
        break


