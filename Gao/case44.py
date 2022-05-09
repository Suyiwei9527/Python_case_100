#两个3行3列的矩阵，实现其对应位置的数据相加并返回一个新矩阵
l=[[12,7,3],[4,5,6],[7,8,9]]
n=[[5,8,1],[14,15,16],[17,18,19]]
Sn=[]
for i in range(3):
    Sn.append([])
    for j in range(3):
        Sn[i].append(l[i][j]+n[i][j])
print(Sn)