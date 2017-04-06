# Dictionary
D = {'food': 'spam', 'quantity': 4, 'color': 'pink'}
print(str(D))

print(D['food'])

D['quantity'] += 1
print(D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print(D)
print(D['name'])

bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'}, 
        'jobs': ['dev', 'mgr'],
        'age': 40.5
}

print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'])
print(rec['jobs'][-1])
rec['jobs'].append('janitor')
print(rec)