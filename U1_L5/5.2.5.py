def add_to_tuple(original, addend):
    tmplist = list(original)
    tmplist.append(addend)
    return tuple(tmplist)


randomlist = []
for i in range (6):
    tmplist=[]
    for j in range (6):
        tmplist.append((j+1)+i*6)
    randomlist.append(tmplist)

row = tuple([])
col = tuple([])

for i in range (6):
    tmprow = randomlist[i]
    tmpcol = []
    for j in range (6):
        tmpcol.append(randomlist[j][i])
    row = add_to_tuple(row,tmprow)
    col = add_to_tuple(col,tmpcol)

rowsum = tuple([])
colsum = tuple([])
for i in range (6):
    tmp_rowsum=0
    tmp_colsum=0
    for j in range (6):
        tmp_rowsum += row[i][j]
        tmp_colsum += col[i][j]
    rowsum = add_to_tuple(rowsum,tmp_rowsum)
    colsum = add_to_tuple(colsum,tmp_colsum)

print("rowsum:",rowsum)
print("colsum:",colsum)