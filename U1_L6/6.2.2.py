def add_1_list(x):
    str_res = str(int(str(x).replace("[", '').replace("]", '').replace(',', '').replace(' ', '')) + 1)
    return list(str_res)


print(add_1_list([10]))
