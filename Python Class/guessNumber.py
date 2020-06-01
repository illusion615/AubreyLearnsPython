# This is a guess number game
import random
secretNumber = random.randint(1, 1000000000000000)
print("I'm thinking of number between 1 to .")
# ask player to guess six times
for guessTaken in range(1, 1000000000000):
    print("Take a guess(#" + str(guessTaken) + ")")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # This condition is the correct guess

if guess == secretNumber:
    print("Great job, you guess my number in " + str(guessTaken) + " guesses.")
else:
    print("Nope, the number i was thinking of was " + str(secretNumber))
