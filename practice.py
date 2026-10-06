# practice.py - Interactive Python Practice Hub
import random

def show_banner():
    print("=" * 48)
    print("  🚀 Welcome to Forkan's Python Practice Hub! 🚀")
    print("=" * 48)

def calculator():
    print("\n--- 🧮 Quick Math Helper ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Choose operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else "Error (Cannot divide by 0)"
        else:
            result = "Invalid operator"

        print(f"✅ Result: {num1} {op} {num2} = {result}")
    except ValueError:
        print("⚠️ Please enter valid numbers.")

def number_guessing_game():
    print("\n--- 🎯 Secret Number Guessing Game ---")
    secret = random.randint(1, 10)
    attempts = 3

    while attempts > 0:
        try:
            guess = int(input(f"Guess a number between 1 and 10 ({attempts} attempts left): "))
            if guess == secret:
                print("🎉 Bingo! You guessed the correct number!")
                return
            elif guess < secret:
                print("📈 Too low, try higher!")
            else:
                print("📉 Too high, try lower!")
            attempts -= 1
        except ValueError:
            print("⚠️ Please enter a whole number.")

    print(f"❌ Game over! The secret number was: {secret}")

def main():
    show_banner()
    while True:
        print("\nChoose what you want to do:")
        print("1. Run Calculator")
        print("2. Play Guessing Game")
        print("3. Exit")
        choice = input("Enter choice (1, 2, or 3): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            number_guessing_game()
        elif choice == "3":
            print("\n👋 Goodbye! Happy coding!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
as
