import random
print('The Number Guessing Game')

no=random.randint(1,10)

print ('guess a number between 1 to 10')

chances=0
while(chances<3):
    guess=int(input('enter your guess '))
    if(guess==no):
        print('Congratulations! You won')
        break
    elif(guess<no):
        print('Please guess a higher number! ', guess)
    else:
        print('Please guess a lower number! ',guess)
    chances=chances+1
        
if(chances==3):
    print('Sorry you loose')