from objects import *
from functionClasses import *

person1 = person('ashraf', 21, 'aashraf9919@gmail.com', 193)
print('person name is', person1.name, 'and height is', person1.height, 'cm')


stu = student('ali', 10, 'ali@ccna.eg', 10, 100010101, 393733, 1)

print(stu.name)


# function classes
funcRating1 = employee('ash', 1000, 5, 60)
funcRating2 = employee('lala', 3000, 4, 50)

print(funcRating1.ratingRate())
print(funcRating2.ratingRate())

funcRating1.bonus()
funcRating2.bonus()