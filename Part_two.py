# Welcome message. informing the user of the parameters. 
print ("Lets play a little game and see if you can guess my number.")
print ('The number will be between 1 & 100. ')
print ("Your guidance system will be the classic too big & too small")

#Defines the random module for this speciifc code so we can generate a random number each time. 
import random
#Sets a random integer to the variable GUESS. 
GUESS = random.randint(1,100)

#Begins a loop.
while GUESS:
    #Requesting user guess via input function.
    user_input = input ("Enter your guess:")
    #Converting user guess into integer.
    user_guess = int(user_input) 
    #If function, seeing if user guess is equal to random generated number.
    #if true, function prints a congratulations text and breaks the loop. 
    if user_guess == GUESS :
        print("CONGRATULATIONS! you did it!")
        break
    #First Elif statement, seeing if user guess is less than random generated number.
    #If true, function prints a "too small" message and returns to user input. 
    elif user_guess < GUESS :
        print("OOF, too small.")
    #Second Elif statement, seeing if user guess is greater than 100.
    #If true, function prints a "I said within 1 & 100" message and returns to user input.         
    elif user_guess > 100:
        print ("Whoa there buddy! i said within 1 & 100.")
    #Else statement, all other functions checked, will print a message to the user saying "too big" 
    # and return to user input. 
    else:
        print("Oof, too big. ")
    










    