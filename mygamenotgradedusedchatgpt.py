import random

def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy (1–50, 10 tries)")
    print("2. Medium (1–100, 7 tries)")
    print("3. Hard (1–200, 5 tries)")
    
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == "1":
        return 50, 10
    elif choice == "2":
        return 100, 7
    elif choice == "3":
        return 200, 5
    else:
        print("Invalid choice, defaulting to Medium.")
        return 100, 7

def play_game():
    max_num, attempts = choose_difficulty()
    secret_number = random.randint(1, max_num)
    
    print(f"\nI'm thinking of a number between 1 and {max_num}.")
    print(f"You have {attempts} attempts to guess it.\n")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempt} tries.")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        
        # Hint system
        if abs(secret_number - guess) <= 5:
            print("🔥 Very close!")
        elif abs(secret_number - guess) <= 15:
            print("🌡️ Getting warmer!")
        else:
            print("❄️ Cold!")
    
    print(f"\n😢 Out of attempts! The number was {secret_number}.")

def main():
    print("=== Number Guessing Game ===")
    
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
    