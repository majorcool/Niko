class People:
    def talk(self):
        print('Ahhhh')


class Infant:
    def talk(self):
        return None
#https://docs.python.org/3/library/exceptions.html#NotImplementedError
"""
Note It should not be used to indicate that an operator or method is not meant to be supported at all – in that case either leave the operator / method undefined or, if a subclass, set it to None.
"""

