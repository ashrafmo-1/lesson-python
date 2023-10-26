for letter in 'hello python':
    print(letter)


print('=============arrays=============')
frinds = ['pikachu', 'elshenawy', '7amada']
for index in frinds:
    print(index)


print('=============range of numbers=============')
for i in range(1, 11):
    print(i)


shhelas = ['lala', 'sasa', 'tata']
for index in range(len(shhelas)):
    print(shhelas[index])


print('# for and if condition even or odd number')
for i in range(10):
    if i % 2 == 0:
        print(i, ' even number')
    else:
        print(i, ' odd number')


print('# search form string in array py for loop and if condition')
words = ['string', 'odd', 'even', 'number', 'boolian', 'true', 'false']
for index in range(len(words)):
    if words[index] == 'boolian':
        print(index, ' iam the boolian value')
    elif words[index] == 'odd':
        print(index,' iam the odd value')
        break
    else:
        print(index, ' iam not boolian value')
else:
    print('not found value')