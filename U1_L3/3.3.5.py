for i in range (1,5):
    for j in range (1,5):
        for k in range (1,5):
            if i == j or i == k:
                continue
            if j == k :
                continue
            print(i,j,k)
