import random, os, time

# List containing each team possible as a word of choice
listOfTeams = ["portugal", "spain", "germany", "england"]

# Empty list that will capture all the letters picked
letterPicked = []

# Amount of lives at the beginning is 6
lives = 6

# Pick a random word from the list
word = random.choice(listOfTeams)

# Infinite loop to keep the game running
while True:
    time.sleep(3)
    os.system("clear")  # Clear the screen for a clean interface

    # Prompt the user to choose a letter and store it in 'letter'
    letter = input("Choose a letter>> ")

    # Check if the letter has been picked before
    if letter in letterPicked:
        print("You have already picked that letter before")
        continue  # Skip the rest of the loop if the letter was already picked

    # If the letter is not in the letterPicked list, add it to the list
    letterPicked.append(letter)

    # Check if the letter is in the randomly generated word
    if letter in word:
        print("Well done, you found a letter")
    else:
        print("Incorrect, letter is not in the word")
        lives -= 1  # Decrement the lives if the guess is incorrect

    # Variable to track if all letters in the word have been guessed
    allLetters = True
    print()

    # Loop through each letter in the word to display progress
    for i in word:
        if i in letterPicked:
            print(i, end="")  # Print the letter if it has been guessed
        else:
            print("_", end="")  # Print an underscore for letters not guessed
            allLetters = False  # Set allLetters to False if any letter is missing
    print()

    # Check if the word has been completely guessed
    if allLetters:
        print("Congratulations! You guessed the word!")
        break  # Exit the loop if the word is fully guessed

    # Check if the player has run out of lives
    if lives == 0:
        print("Game over! The word was:", word)
        break  # Exit the loop if no lives are left


    if allLetters:
        print(f"Congrats!!, you won with {lives} left!")
        break

    if lives<=0:
        print(f"better luck next time, the correct word was {word} ")
        break
    else:
        print(f"You have only {lives} left")
