def no_rome(rome_str):
    result = 0
    dict_special_case = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    for key in dict_special_case:
        result += rome_str.count(key) * dict_special_case[key]
        rome_str = rome_str.replace(key, '')
    dict_normal_case = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for key in dict_normal_case:
        result += rome_str.count(key) * dict_normal_case[key]
        rome_str = rome_str.replace(key, '')
    return result


print(no_rome('III'))
