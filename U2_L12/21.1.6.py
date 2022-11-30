original_f = open("4.txt", "r")
output_f = open("result4.txt", "w")
char = original_f.read(1)
while char != "":
    if char.isupper():
        char = char.lower()
    elif char.islower():
        char = char.upper()

    output_f.write(char)
    print(char)
    char = original_f.read(1)
