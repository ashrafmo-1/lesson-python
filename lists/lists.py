list = ["js", "py", "html", "css", ["sass", "bootStrap"]]
list[4] = ["sass", "bootStrap", "html", "css", 'java'] #update index 4

print(list[0])
print(list[0: 3])
print(list[1:])
print(list[-1]); print(list[4])

# concatenate lists fot example by function extend()
ProgrammingLanguage = ["js", "py", "html", "css", "sass", "bootStrap"]
Language = ['arabic', 'english', 'turkish', 'spanish']
# for example [0]                     # for example [1]
ProgrammingLanguage.extend(Language); ProgrammingLanguage += Language

print(ProgrammingLanguage)



# add new values to the list end by function append()
foods = ['apple', 'panana', 'orange']
foods.append('pathish end')

print(foods)

# add new values to the list in any location by function insert()
food = ['apple', 'panana', 'orange']
food.insert(0, 'pathish')
food.insert(1, 'pathish')
food.insert(-2, 'pathish')
print(food)


names = ['ashraf', 'mohamed', 'ali', 'mahmoud']
# remove value from the list by function remove()
names.remove('mohamed')
# remove all values from the list by function clear()
names.clear()
# cut from the list and copy from any location
# names.pop(0)

print(names)


# count the duplcat value in the list
names = ['ashraf','mohamed', 'ali','mohamed', 'lala']
print(names.count('mohamed'))
# sort the list by function sort()
names.sort() # make ordering list
print(names)