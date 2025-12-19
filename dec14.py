import random
import os

SCORE_FILE = "best_score.txt"

def load_best_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return int(f.read())
    return None
# Save the best score to a file
def save_best_score(score):
    with open(SCORE_FILE, "w") as f:
        f.write(str(score))
#difficulty level
def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy   (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard   (1–200, 5 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return 50, 10
        if choice == "2":
            return 100, 7
        if choice == "3":
            return 200, 5
        print("❌ Invalid choice.")

def give_hint(guess, number):
    diff = abs(guess - number)
    if diff == 0:
        return
    if diff <= 5:
        print("🔥 Very hot!")
    elif diff <= 10:
        print("🌡️ Warm")
    else:
        print("❄️ Cold")

def play_game():
    print("\n🎯 Number Guessing Game")
    max_number, max_attempts = choose_difficulty()
    number = random.randint(1, max_number)

    attempts = 0
    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts. Type 'q' to quit.")

    while attempts < max_attempts:
        guess = input("\nYour guess: ").strip()

        if guess.lower() == "q":
            print(f"👋 You quit! The number was {number}.")
            return

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
            return attempts

        give_hint(guess, number)
        print(f"Attempts left: {max_attempts - attempts}")

    print(f"\n💀 Out of attempts! The number was {number}.")
    return None

def main():
    best_score = load_best_score()

    if best_score:
        print(f"🏆 Best score: {best_score} attempts")

    while True:
        result = play_game()

        if result:
            if best_score is None or result < best_score:
                save_best_score(result)
                best_score = result
                print("🏆 New best score!")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! 👾")
            break

if __name__ == "__main__":
    main()
