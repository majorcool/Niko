def add_to_tuple(original, addend):
    tmplist = list(original)
    tmplist.append(addend)
    return tuple(tmplist)

shopping_cart = tuple([])

while (1):
    item = input('item=')
    if item == 'q':
        break
    shopping_cart = add_to_tuple(shopping_cart,item)

print('There are',len(shopping_cart) ,'items in cart')

for i in range (0,len(shopping_cart)):
    print(shopping_cart[i],end = ' ')