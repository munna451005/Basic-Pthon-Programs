import math
from audioop import findmax

score=[70,90,60,50,25,65,85]

total=  0
max=score[0]
for x in score:
    total= total+x
    average=total/len(score)
    if max<x:
        max=x
print("Total number is: ",total)
print("Total average is: ",math.ceil(average))
print("Maximum is",max)