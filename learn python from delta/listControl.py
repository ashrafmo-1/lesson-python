my_list = [1, 2, 3, 4, 5]

print(my_list[0])
print(my_list[1:4])
print(my_list[2: ])
print(my_list[3: -1])

my_list.append(6)
print(my_list)

length = len(my_list)
index = my_list.index(4) # ==> get the index of the first element

my_list.insert(0, 7) # replace the zero number with the seven number
print(my_list)

my_list.remove(3)  # Remove the first occurrence of 3
print(my_list)

popped_element = my_list.pop(1)  # Removes and returns the last element
print(popped_element)

my_list.sort() # ==> sorted list

repeated_list = my_list * 3  # repeated list three times

print(repeated_list)