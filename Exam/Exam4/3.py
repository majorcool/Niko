def str_revert(n, str='123456789'):
    answer = ""
    n_leftover = len(str) % n
    for i in range(len(str) // n):
        for j in range(n):
            answer += str[i*n+(n-j-1)]
    for i in range(n_leftover):
        answer += str[-(i+1)]
    return answer

print(str_revert(3,'abcdefghi'))
