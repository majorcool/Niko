original_f = open("whatever.txt", "r")
output_f = open("whatever_copy.txt", "w")
char = original_f.readline()
while char != "":
    output_f.write(char)
    char = original_f.readline()
