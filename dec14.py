import random

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'q' to quit at any time.\n")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Your guess: ").strip()

        if guess.lower() == 'q':
            print(f"👋 You quit! The number was {number}.")
            break

        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! 👾")
            break
        print()

if __name__ == "__main__":
    main()