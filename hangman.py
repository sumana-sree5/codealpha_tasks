import random

def hangman():
    # 5 predefined words as per simplified scope guidelines
    words = ["python", "internship", "automation", "developer", "program"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("--- Welcome to CodeAlpha Hangman! ---")
   
    while attempts > 0:
        # Display current word progress
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("\nWord: " + " ".join(display_word))
        print(f"Attempts remaining: {attempts}")
       
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word correctly!")
            return

        guess = input("Guess a letter: ").lower().strip()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Wrong guess! '{guess}' is not in the word.")
            attempts -= 1

    print(f"\n💀 Game Over! The correct word was: '{secret_word}'")

if __name__ == "__main__":
    hangman()
