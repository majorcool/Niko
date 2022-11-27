class ScoreError(Exception):
    pass


def input_score():
    scr_string = input()
    if scr_string.find(".") != -1 and scr_string.find(".") < len(scr_string) - 3:
        raise ScoreError
    return float(scr_string)


students_scr = []
for i in range(30):
    flag = True
    while flag:
        try:
            students_scr.append(input_score())
        except ScoreError:
            print("输入的数字不符合要求")
        except ValueError:
            print("1输入的不是数字")
        else:
            flag = False
print(students_scr)
