# nameQuestion = input('whats your name:> ')
# ageQuestion = input('how old your you:> ')
# print('my name is ' + '"' + nameQuestion + '"' + ' and my age is ' + '"' + ageQuestion + '"')

# make function
def sayQuestion():
    nameQuestion = input('whats your name:> ')
    ageQuestion = input('how old your you:> ')
    print('my name is'+ '"' + nameQuestion + '"' +'and my age is'+ '"' + ageQuestion + '"')

sayQuestion()

# function maked to dont repeat yourself
def sayhello():
    nameQuestion = input('hello:> ')
    print('your say is:> ' + nameQuestion)

sayhello()