# A guessing game where computer tries to guess a number being defined by a man.
# The number must lie in the range of 100.

import time, sys

def displayInstruct():
    '''Displays an instuction for the player.'''
    msg = 'Welcome to the guessing game!\n'
    msg += 'The computer will find out number you thought of.'
    print(msg)

def askYesNo(question):
    '''Asks a question with a yes or no answer.'''
    response = None
    while response not in 'yes ye y no n'.split():
        response = input(question).lower()
    return(response)

def agreeNotAgree():
    '''Asks the player if he wants to play.'''
    will = askYesNo('Would you like to play a guessing game? yes/no ')
    if will.startswith('y'):
        print()
        msg = 'Let us do it!\n'
        msg += 'Think of a number that lies between 1 and 100.'
        print(msg)
    else:
        print('Leaving this place!')
        sys.exit()

def congrat():
    '''Congratulates computer on guessing the number.'''
    print('The game is over! The computer was quick to guess it! Try another number.')

def playAgain():
    '''Returns True if the player wants to play again, otherwise it returns False.'''
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

numbers = list(range(1,101))

def main():
    while True:
        displayInstruct()
        print
        agreeNotAgree()
        low = 0
        high = len(numbers)-1
        
        time.sleep(3)
        while low <= high:
            mid = int((low+high)/2)
            print
            guess = askYesNo('Is it ' + str(numbers[mid]) + ' (yes/no)? ')
            if guess.startswith('y'):
                print('I, the Computer, found the number! It is ' + str(numbers[mid]) + '!')
                break
            if guess.startswith('n'):
                guess = askYesNo('Is the number bigger? (yes/no)? ')
                if guess.startswith('y'):
                    low = mid+1
                else:
                    high = mid-1

        print
        congrat()

        if not playAgain():
            break

main()
