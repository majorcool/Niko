def capitalize_title(title: str) -> str:
    result = ""
    tittle_splitted = title.split(" ")
    for i in tittle_splitted:
        if len(i) <= 2:
            result += (i.lower() + " ")
        else:
            result += (i[0].upper() + i[1:].lower() + " ")
    return result

print(capitalize_title("First leTTeR of EACH Word"))