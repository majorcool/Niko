def count_prefix(words, prefix):
    count = 0
    for i in words:
        if i.find(prefix) == 0:
            count += 1
    return count


words = ["coopedu","win","loops","success"]
pref = "code"
print(count_prefix(words,pref))