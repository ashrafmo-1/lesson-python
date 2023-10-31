10 # full calculation

numberOne = float(input('inter number one:> '))
operator = input('inter operator')
numberTwo = float(input('inter number two:> '))

if operator == '+':
    print(numberOne + numberTwo)
elif operator == '-':
    print(numberOne - numberTwo)
elif operator == '*':
    print(numberOne * numberTwo)
elif operator == '/':
    print(numberOne / numberTwo)
elif operator == '^':
    def powFirstExample(numberOne, numberTwo):
        return numberOne ** numberTwo
print(powFirstExample(numberTwo, numberTwo))