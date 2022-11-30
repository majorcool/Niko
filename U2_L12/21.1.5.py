original_f = open("3.txt", "r")
encrypted_f = open("result_3.txt", "w")

char = original_f.read(1)
while char != "":
    if char.isalpha():
        if char == 'Z':
            char = 'A'
        elif char == 'z':
            char = 'a'
        else:
            char = chr(ord(char) + 1)
    encrypted_f.write(char)
    print(char)
    char = original_f.read(1)
original_f.close()
encrypted_f.close()