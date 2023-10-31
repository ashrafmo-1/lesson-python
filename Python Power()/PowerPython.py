# exponent function

# example one
def powFirstExample(f_num, powNumber):
    return f_num ** powNumber
print(powFirstExample(2, 3))

# example two
def powSecondExample(f_num, powNumber):
    result = 1
    for index in range(powNumber):
        result = result * f_num
    return result
print(powSecondExample(3, 3))