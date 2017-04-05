# List
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('M[1] = ' + str(M[1]))
print('M[1][2] = ' + str(M[1][2]))

# Comprehensions
print('col2 = [row[1] for row in M] = ' + str([row[1] for row in M]))
print('M = ' + str(M))
print('[row[1] for row in M if row[1] % 2 == 0] = ' + str([row[1] for row in M if row[1] % 2 == 0]))
print('diag = [M[i][i] for i in [0, 1, 2]] = ' + str([M[i][i] for i in [0, 1, 2]]))
print('doubles = [c * 2 for c in "spam"] = ' + str([c * 2 for c in "spam"]))
print('list(range(4)) = ' + str(list(range(4))))
print('list(range(-6, 7, 2)) = ' + str(list(range(-6, 7, 2))))
print('[[x ** 2, x ** 3] for x in range(4)] = ' + str([[x ** 2, x ** 3] for x in range(4)]))
print('[[x, x/2, x * 2] for x in range(-6, 7, 2) if x > 0] = '
      + str([[x, x/2, x * 2] for x in range(-6, 7, 2) if x > 0]))

# Generator
G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

# Map
list(map(sum, M))
print(str(list(map(sum, M))))

# Set
{sum(row) for row in M}
print(str({sum(row) for row in M}))

# Dictionary
{i:sum(M[i]) for i in range(3)}
print(str({i:sum(M[i]) for i in range(3)}))

# Comprehensions for lists, sets, dictionaries, and generators
[ord(x) for x in 'spaam']
print(str([ord(x) for x in 'spaam']))

{ord(x) for x in 'spaam'}
print(str({ord(x) for x in 'spaam'}))

{x:ord(x) for x in 'spaam'}
print(str({x:ord(x) for x in 'spaam'}))

(ord(x) for x in 'spaam')
print(str(next((ord(x) for x in 'spaam'))))

