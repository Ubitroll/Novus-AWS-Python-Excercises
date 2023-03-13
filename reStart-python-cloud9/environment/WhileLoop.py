import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Generate a random number
number = random.randint(1,10)
isGuessRight = False

# While the player hasn't guessed correctly
while isGuessRight != True:
    # Ask them to guess
    guess = input("Guess a number between 1 and 10 = ")
    # Check if guess was correct
    if int(guess) == number:
        ## If correct then tell them they won and end loop
        print("You guessd {}. That is correct! You win!".format(guess))
        isGuessRight = True
    # Else tell them they are wrong and start again
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))