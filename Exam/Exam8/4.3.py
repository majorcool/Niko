def hamming_distance(x: int, y: int) -> int:
    bin_str_x = str(bin(x)).lstrip("0b")
    bin_str_y = str(bin(y)).lstrip("0b")
    max_len = max(len(bin_str_y), len(bin_str_x))
    bin_str_y = bin_str_y.zfill(max_len)
    bin_str_x = bin_str_x.zfill(max_len)
    print(bin_str_y)
    print(bin_str_x)
    hamming_dist = 0
    for i in range(max_len):
        if bin_str_y[i] != bin_str_x[i]:
            hamming_dist += 1
    return hamming_dist


x = 3
y = 1
print(hamming_distance(x, y))
