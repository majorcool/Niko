def update_dict(dict_sample):
    tmp_val = int(input("val="))
    tmp_key = input("key=")
    if tmp_key in dict_sample:
        dict_sample.update({tmp_key: max(dict_sample[tmp_key], tmp_val)})
    else:
        dict_sample.update({tmp_key: tmp_val})
    return dict_sample


print(update_dict({"test": 114}))
