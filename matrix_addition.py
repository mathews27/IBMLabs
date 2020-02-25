X = [[12, 7, 3],
     [4, 5, 6],
     [3, 7, 5]]
Y = [[12, 7, 3],
     [4, 5, 6],
     [3, 7, 5]]
R = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        R[i][j] = X[i][j] + Y[i][j]

for i in range(len(R)):
    for j in range(len(R[0])):
        print(R[i][j], end=" ")
    print()