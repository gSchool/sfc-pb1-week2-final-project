"""
Week 2 Final Project - Starter Code
Console Application Template

This is a basic structure to get you started. Modify it for your project!
"""

import quiz_engine 

quiz_engine.run_lotr()
quiz_engine.run_darksouls()


def display_menu():
    print("\n")
    print("=" * 65)

    print(r"""
   ██████╗ ██╗   ██╗██╗███████╗
  ██╔═══██╗██║   ██║██║╚══███╔╝
  ██║   ██║██║   ██║██║  ███╔╝
  ██║▄▄ ██║██║   ██║██║ ███╔╝
  ╚██████╔╝╚██████╔╝██║███████╗
   ╚══▀▀═╝╚═╝╚═════╝ ╚═╝╚══════╝
""")

    print("    The Perfect Python Quiz for NERDS")
    print("=" * 65)

    print("\nChoose your challenge:\n")
    print("  1) ⚔️  Lord of the Rings Quiz")
    print("  2) 🔥  Dark Souls Quiz")
    print("  3) 📜  Lore Mode (stretch goal)")
    print()
    print("  help  - Show menu")
    print("  quit  - Exit the quiz")
    print("\n" + "=" * 65)


def handle_choice(choice):
    """
    Process the user's choice and call appropriate functions.

    Returns:
        bool: True to continue, False to exit
    """
    if choice == "1":
        print("⚔️ Starting Lord of the Rings Quiz...\n")
        # Change filename to whatever your LOTR lore file is actually named:
        quiz_engine.run_quiz("lotr_lore.json")

    elif choice == "2":
        print("🔥 Starting Dark Souls Quiz...\n")
        # Change filename to whatever your Dark Souls lore file is actually named:
        quiz_engine.run_quiz("darksouls_lore.json")

    elif choice == "3":
        print("📜 Lore Mode coming soon (stretch goal).")
        # Later you could do: quiz_engine.run_lore_mode(...)

    elif choice == "help":
        display_menu()

    elif choice == "quit":
        print("Thanks for playing. Goodbye!")
        return False

    else:
        print(f"'{choice}' is not a valid option. Type 'help' to see available commands.")

    return True


def main():
    print("Welcome to the Console Application!")
    display_menu()

    running = True
    while running:
        choice = input("Enter your choice: ").strip().lower()
        running = handle_choice(choice)


if __name__ == "__main__":
    main()