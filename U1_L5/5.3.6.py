def compare_dic(dict1, dict2):
    dict1_keys = dict1.keys()
    dict2_keys = dict2.keys()
    count = 0
    pairs = []
    for i in dict1_keys:
        for j in dict2_keys:
            if i == j and dict1[i] == dict2[j]:
                count += 1
                pairs.append((i, dict1[i]))
    return tuple([count]+pairs)


dict_1 = {"key1":1, "key2":2}
dict_2 = {"key1":1, "key2":1}
print(compare_dic(dict_1,dict_2))