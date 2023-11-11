#  try except errors




try:
    val = float(input('type your phone number:> '))
    print(val)
    res = 20 / 0
except ZeroDivisionError as zeroError:
    print('Error', zeroError)
except ValueError as errorStr:
    print(errorStr)

print('code is work')