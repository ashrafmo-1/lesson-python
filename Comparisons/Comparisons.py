# Comparisons => number, string, boolean, list

# make built-in function :> max()

def max_num(numOne, numTwo, numThree):
    if numOne >= numTwo and numOne >= numThree:
        return numOne
    elif numTwo >= numOne and numTwo >= numThree:
        return numTwo
    else:
        return numThree

print(max_num(1000, 2000, 3000))
print(max(1000, 2000, 3000))

# make built-in function :> min()
def min_num(numOne, numTwo, numThree):
    if numOne <= numTwo and numTwo <= numThree:
        return numOne
    elif numTwo <= numOne and numTwo <= numThree:
        return numTwo
    else:
        return numThree

print(min_num(1000, 2000, 3000))
print(min(1000, 2000, 3000))

# match strting if one if including two
def matchString(strOne, strTwo):
    if strOne == strTwo:
        return 'string is matching'
    else:
        return 'string is not matching'

print(matchString('hell00o', 'hello'))