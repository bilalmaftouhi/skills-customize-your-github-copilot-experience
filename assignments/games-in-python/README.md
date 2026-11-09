# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic word-guessing game to practice Python strings, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Choose a Word and Track Guesses

#### Description
Create the core of a Hangman game. The game should choose a word from a predefined list and keep track of the player's correct and incorrect letter guesses.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list.
- Accept one letter guess at a time.
- Show the correctly guessed letters in their matching positions and use underscores for letters that have not been guessed.
- Track incorrect guesses and show how many attempts remain.
- Avoid counting a letter that the player has already guessed a second time.

### 🛠️ Play and Finish the Game

#### Description
Let the player continue guessing until they reveal the word or run out of attempts, then clearly show the result.

#### Requirements
Completed program should:

- Repeat the prompt and display updated word progress after each guess.
- End when the player guesses every letter in the secret word or runs out of incorrect guesses.
- Display a clear win or loss message.
- Reveal the secret word when the player loses.
