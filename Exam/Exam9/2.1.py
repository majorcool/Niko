def try_finally_1():
    try:
        print("trying whatever")
    finally:
        print("finally")

    print("return")
    return

def try_finally_2():
    try:
        print("trying whatever")
        print("return")
        return
    finally:
        print("finally")


try_finally_1()
print("-------")
try_finally_2()

"""
若try内部返回，则finally在返回之后执行 
若return在try外部，则finally在返回之前执行
"""