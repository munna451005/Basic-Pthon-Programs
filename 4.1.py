from audioop import avgpp

score=[70,90,60,50,25,65,75]
# 1

x = sum(score)
average=x/len(score)
maximum=max(score)
for x in score:
    print(f"element:{x},sum:{score},average:{average},maximum:{maximum}")