dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
print("len=",len(dic))
dic.update({'java': 98})
dic.pop('c')
dic.update({'php': 90})
key_list = dic.keys()
value_list = dic.values()
print("javascript" in dic)
sumans = sum(value_list)
maximum = max(value_list)
minimum = min(value_list)
dic1 = {'php': 97}
dic.update(dic1)