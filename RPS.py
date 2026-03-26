import random

def CmpWin():
    print('Computer Win')

def PlWin():
    print('You Win')


choices = ['Rock', 'Paper', 'Scissor']

plch = input('Choice between Rock, Paper, Scissor : ').capitalize()

cmpch = random.choice(choices)

print('Your Choice : ', plch)

print('Computer Choice : ',cmpch)

if cmpch == plch:
    print('Draw')
elif cmpch == 'Rock' and plch == 'Scissor':
    CmpWin()
elif cmpch == 'Rock' and plch == 'Paper':
    PlWin()
elif cmpch == 'Paper' and plch == 'Rock':
    CmpWin()
elif cmpch == 'Paper' and plch == 'Scissor':
    PlWin()
elif cmpch == 'Scissor' and plch == 'Rock':
    PlWin()
elif cmpch == 'Scissor' and plch == 'Paper':
    CmpWin()
else: 
    print('Invalid Choice')