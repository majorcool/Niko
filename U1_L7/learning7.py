'''
https://docs.python.org/3/library/functions.html

The Python interpreter has a number of functions and types built into it that are always available

print()
abs()

'''

def factorial (n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def fat_wave_nazi(f):
    if f == 0 or f == 1:
        return f
    return fat_wave_nazi(f-1) + fat_wave_nazi(f-2)

print(fat_wave_nazi(10))