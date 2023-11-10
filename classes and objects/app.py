from objects import *

person1 = person('ashraf', 21, 'aashraf9919@gmail.com', 193)
print('person name is', person1.name, 'and height is', person1.height, 'cm')


stu = student('ali', 10, 'ali@ccna.eg', 10, 100010101, 393733, 1)
print(stu.name)



# function classes <====================================
from functionClasses import *

funcRating1 = employee('ash', 3000, 5, 60)
funcRating2 = employee('lala', 3000, 4, 50)

print(funcRating1.ratingRate())
print(funcRating2.ratingRate())

print(funcRating1.salary)
funcRating1.bonus()
print(funcRating2.salary)
funcRating2.bonus()