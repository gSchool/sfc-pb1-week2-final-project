"""
Week 2 Final Project - Starter Code
Console Application Template

This is a basic structure to get you started. Modify it for your project!
"""

import quiz_engine
LOTR_FILE = "data/lotr.json"
DARK_SOULS_FILE = "data/dark_souls.json"


def display_menu():
    print("\n" + "=" * 65)
    print(r"""
   ██████╗ ██╗   ██╗██╗███████╗
  ██╔═══██╗██║   ██║██║╚══███╔╝
  ██║   ██║██║   ██║██║  ███╔╝
  ██║▄▄ ██║██║   ██║██║ ███╔╝
  ╚██████╔╝╚██████╔╝██║███████╗
   ╚══▀▀═╝╚═╝╚═════╝ ╚═╝╚══════╝
""")
    print("    The Perfect Python Quiz for Fans")
    print("=" * 65)
    print("\nChoose your challenge:\n")
    print("  1) ⚔️  The One Ring Trial  — Lord of the Rings")
    print("  2) 🔥  Kindle the Flame    — Dark Souls")
    print("  3) 📜  Lore Mode (stretch goal)")
    print()
    print("  help  - Show menu")
    print("  quit  - Exit the quiz")
    print("\n" + "=" * 65)

def handle_choice(choice):
    if choice == "1":
        print("⚔️ Starting Lord of the Rings Quiz...\n")
        quiz_engine.run_quiz(LOTR_FILE)

    elif choice == "2":
        print("🔥 Starting Dark Souls Quiz...\n")
        quiz_engine.run_quiz(DARK_SOULS_FILE)

    elif choice == "3":
        print("📜 Lore Mode coming soon (stretch goal).")

    elif choice == "help":
        display_menu()

    elif choice == "quit":
        print("Thanks for playing. Goodbye!")
        return False

    else:
        print(f"'{choice}' is not a valid option. Type 'help' to see available commands.")

    return True

def main():
    display_menu()
    running = True
    while running:
        choice = input("Enter your choice: ").strip().lower()
        running = handle_choice(choice)

if __name__ == "__main__":
    main()