for i in range (1,5):
    for j in range (1,5):
        for k in range (1,5):
            for l in range (1,5):
                if i == j or i == k or i == l:
                    continue
                if j == k or j == l:
                    continue
                if k == l:
                    continue
                print(i,j,k,l)
