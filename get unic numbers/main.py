Allnumbers = [1, 2, 3, 9, 10, 11, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 9, 10, 3, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

uniqueNUms = []

for number in Allnumbers:
    if number not in inuqeNUms:
        inuqeNUms.append(number)

print(inuqeNUms)