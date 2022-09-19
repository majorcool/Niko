num=1
sumchi=0 # chicken
sumcou=0 # couple
while num <= 100:
    if num%2==0:
        sumcou+=1
    else:
        sumchi+=1
    num +=1
print("偶：",sumcou,"鸡",sumchi)