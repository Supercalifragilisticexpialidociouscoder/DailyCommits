import random
import time

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def random_quote():
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "First, solve the problem. Then, write the code.",
        "Experience is the name everyone gives to their mistakes.",
        "In order to be irreplaceable, one must always be different.",
        "Java is to JavaScript what car is to Carpet."
    ]
    return random.choice(quotes)

def main():
    typewriter("Welcome to the Random Programmer Quote Generator!!!\n")
    while True:
        typewriter(f"\n💡 {random_quote()}\n")
        again = input("Want another quote? (y/n): ").strip().lower()
        if again != 'y':
            typewriter("Goodbye! Keep coding! 🚀")
            break


if __name__ == "__main__":
    main()