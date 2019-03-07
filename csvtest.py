import csv

'''
Set Up
'''

file = 'test.csv'

with open(file) as f:
    d = dict(filter(None, csv.reader(f)))


matches = []
with open(file) as f:
    reader = csv.reader(f, delimiter=",")
    for i in reader:
        matches.append(i[0])

# print(matches)

search = input('Search Term: ')

indices = [i for i, s in enumerate(matches) if search in s]
pos = 1

if len(indices) == 1:
    print(d[matches[indices[0]]])

elif len(indices) > 1:
    for i in indices:
        print('%s)' % pos, d[matches[i]], matches[i])
        pos += 1
    select = input('Select Test: ')
    if select.isdigit() == True and int(select) <= len(indices):
        print(d[matches[indices[int(select)-1]]])
    else:
        print('invalid selection')

else:
    print('no matches')