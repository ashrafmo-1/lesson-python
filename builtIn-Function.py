# all built-in functions used in this module

#### starting built-in functions for numbers ####
# max => get height number
# min => get small number
# round => Rounding to the nearest number
# floor => Rounding to the smallest number "main import from math => from math import floor"
# ceil => Rounding to the largest number "main import from math => from math import floor"
# sqrt => Quadratic Islands || الجزر التربيعي
# pow => for example pow(10, 4) => 10 * 10 * 10 * 10


#### starting built-in functions for strings ####
# lower
# upper
# islower
# isupper
# len
# index
# replace


#----------------------------------------------------------------
print("#### starting built-in functions for numbers ####")     #|
print(max(10, 99))                                             #|
print(min(10, 99))                                             #|
print(pow(10, 4))                                              #|
print(round(10.6))                                             #|
                                                               #|
from math import floor                                         #|
print(floor(10.6))                                             #|
                                                               #|
from math import ceil                                          #|
print(ceil(10.2))                                              #|
                                                               #|
from math import sqrt                                          #|
print(sqrt(100))                                               #|
#----------------------------------------------------------------

print("#### starting built-in functions for strings ####")
print("#################################################")
name = 'ashraf'
namecapital = 'MOHAMED'
stady = 'in_delta'

print(name.upper())
print(namecapital.lower())
print(name.islower())
print(name.isupper())
print(namecapital.islower())
print(namecapital.isupper())

print(len(name))
print(name.index('a'))
print(name.replace('ashraf', 'ASHRAF'))