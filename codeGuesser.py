from __future__ import print_function  
import random   # Required to generate random numbers

digits = random.randint(0,999)  # Generates a random number between 0 and 999 (inclusive)
code = str(digits).zfill(3)     # If the number is less than 100, e.g. 45, then it will place a zero in front if it -> 045
codeList = [int(x) for x in str(code)]  # Convert numbers into list e.g. 123 becomes [1,2,3]

while True:
    guess = input('Guess the code: ')                   # Ask the user to guess
    if guess.isdigit() and len(guess) == 3 :                # Check the guess is a number, otherwise output message
        guessList = [int(x) for x in str(guess)]
        if guessList == codeList:
            correct = True
            break                                           # Break out of the loop if guess is correct
        for i in range(0,3):
            if guessList[i] in codeList:                    # Check if any of the numbers match
                if guessList[i] == codeList[i]:             # Check if they are in the same position
                    print(guessList[i], 'is in the correct position')  
                elif codeList.count(guessList[i]) > 1:      # Check how many times the number appears in the list
                    print(guess[i], ' occurs in the code', codeList.count(guessList[i]), 'times')
                else:
                    print (guess[i], 'is in the code, but not in the correct position')
            else:
                print (guess[i], 'is not in the code')
    else:
        print('Remember to guess with a 3 digit number')    


print("\nWell done!\n")