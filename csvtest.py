import csv

def SOPsearch():
    file = 'test.csv' # CSV data file
    matches = [] # list of strings used to search for SOP name
    pos = 1  # used to identify multiple similarly named tests by position

    # Create Dictionary from Data File
    with open(file) as f:
        d = dict(filter(None, csv.reader(f)))

    # Add names of SOPs to a searchable list
    with open(file) as f:
        reader = csv.reader(f, delimiter=",")
        for i in reader:
            matches.append(i[0])

    print("press 'x' at any time to exit.")

    search = input('search term: ')

    if search == 'x':
        return

    indices = [i for i, s in enumerate(matches) if search in s] # adds matching results to the list


    if len(indices) == 1:
        print(d[matches[indices[0]]],matches[indices[0]])

    elif len(indices) > 1:
        for i in indices:
            print('%s)' % pos, d[matches[i]], matches[i])
            pos += 1

        select = input('select test: ')

        if select.isdigit() == True and int(select) <= len(indices):
            print(d[matches[indices[int(select)-1]]])

        elif select == 'x':
            return

        else:
            print('invalid selection. try again.')
            SOPsearch()

    else:
        print('no matches. try again.')
        SOPsearch()

SOPsearch()
