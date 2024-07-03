# hangman
This repo contains code for a console hangman game i did as part of the #100daysOfReplit code challenge



## Project Description
This is a simple command-line implementation of the classic Hangman game. The game selects a random word from a predefined list of football teams and prompts the player to guess the letters of the word one by one. The player has a limited number of lives, and each incorrect guess reduces the number of lives by one. The game ends when the player either guesses the word correctly or runs out of lives.

## Project Features
- Random selection of words from a list of football teams.
- Input validation to check if a letter has been guessed before.
- Display of the current state of the word with guessed and unguessed letters.
- Tracking of the number of lives remaining.
- Congratulatory message when the player guesses the word correctly.
- Game over message when the player runs out of lives.

## Game Logic
1. Import necessary libraries: `random`, `os`, and `time`.
2. Define a list of football teams.
3. Initialize an empty list to capture all the letters picked by the player.
4. Set the initial number of lives to 6.
5. Randomly select a word from the list.
6. Start an infinite loop to run the game:
   - Pause for 3 seconds and clear the screen.
   - Prompt the player to choose a letter.
   - Check if the letter has been picked before. If yes, display a message and continue.
   - Add the new letter to the list of picked letters.
   - Check if the letter is in the word:
     - If yes, display a congratulatory message.
     - If no, decrement the number of lives and display an incorrect message.
   - Display the current state of the word, showing guessed letters and underscores for unguessed letters.
   - Check if the player has guessed all the letters in the word. If yes, display a congratulatory message and end the game.
   - Check if the player has run out of lives. If yes, display a game over message and end the game.
