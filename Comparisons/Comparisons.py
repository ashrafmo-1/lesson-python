# Comparisons => number, string, boolean, list

# make built-in function :> max()

def max_num(numOne, numTwo, numThree):
    if numOne >= numTwo and numOne >= numThree:
        return numOne
    elif numTwo >= numOne and numTwo >= numThree:
        return numTwo
    else:
        return numThree

print(max_num(100, 20, 300))
print(max(100, 2000, 300))

# match strting if one if including two
def matchString(strOne, strTwo):
    if strOne == strTwo:
        return 'done True'
    else:
        return 'error False'

print(matchString('hell00o', 'hello'))