privet = 'word'
guess = ""
countGuess = 0;lemetGuess = 2
outguess = False

while guess != privet and not outguess:
    if countGuess < lemetGuess:
        guess = input('inter privet WOrd:> ')
        countGuess += 1
    else:
        outguess = True

if outguess == False:
    print("you win")
else:
    print("you loser")