M = [[1,2,3],[4,5,6],[7,8,9]]
print('M[1] = ' + str(M[1]))
print('M[1][2] = ' + str(M[1][2]))
print('col2 = [row[1] for row in M] = ' + str([row[1] for row in M]))
print('M = ' + str(M))
print('[row[1] for row in M if row[1] % 2 == 0] = ' + str([row[1] for row in M if row[1] % 2 == 0]))
print('diag = [M[i][i] for i in [0,1,2]] = ' + str([M[i][i] for i in [0,1,2]]))
print('doubles = [c * 2 for c in "spam"] = ' + str([c * 2 for c in "spam"]))
print('list(range(4)) = ' + str(list(range(4))))
print('list(range(-6, 7, 2)) = ' + str(list(range(-6, 7, 2))))

