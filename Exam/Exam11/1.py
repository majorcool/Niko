#摆

def subsequences(x):
    bin_comp = []
    for i in range(2**len(x)):
        bin_comp.append(str(bin(i)).lstrip("0b").zfill(len(x)))
    return_list = []
    for i in bin_comp:
        current_comp = ""
        for j in range(len(i)):
            if i[j] == '1':
                current_comp += x[j]
        return_list.append(current_comp)
    return return_list


a = input()
b = input()
a_comp = subsequences(a)
b_comp = subsequences(b)
maxlen = 0
max_unsame_comp = ""
for i in a_comp:
    if not i in b_comp and len(i) > maxlen:
        max_unsame_comp = i
        maxlen = len(i)
if maxlen != 0:
    print(maxlen,max_unsame_comp)
else:
    print("-1")