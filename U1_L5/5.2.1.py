menu = ("shit1","shit2","shit3","shit4","shit5")
for i in range(5):
    print(menu[i], end=' ')

#menu[0]="shit6" #TypeError: 'tuple' object does not support item assignment

print("")
menu = ("shit6","shit7","shit3","shit4","shit5")
for i in range(5):
    print(menu[i], end=' ')