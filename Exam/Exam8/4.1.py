def check_if_pangram(sentence: str) -> bool:
    alphabet_occurence = []
    for i in range(0, 26):
        alphabet_occurence.append(0)
    for i in sentence:
        if i.isalpha():
            alphabet_occurence[ord(i) - ord('a')] += 1
    for i in alphabet_occurence:
        if not i:
            return False
    return True


print(check_if_pangram("coopedu"))
