class NotFiveError(Exception):
    pass


def get_list_content(s):
    list_s = s.split(',')
    if len(list_s) != 5:
        raise NotFiveError
    returnlist = []
    for i in list_s:
        returnlist.append(int(i))
    return returnlist


try:
    print(get_list_content("1.1,1e"))
except NotFiveError:
    print("NotFive!")
except ValueError:
    print("int only!")

try:
    print(get_list_content("e,e,e,e,e"))
except NotFiveError:
    print("NotFive!")
except ValueError:
    print("int only!")
