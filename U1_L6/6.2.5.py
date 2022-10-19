def verify_huiwen(s):
    s = s.lower()
    s_verify = ""
    for i in s:
        if i.isnumeric() or i.isalpha():
            s_verify += i
    return s_verify[::-1] == s_verify

print(verify_huiwen("A man, a plan, a canal: Panama"))