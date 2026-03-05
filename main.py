"""
Week 2 Final Project - Starter Code
Console Application Template

This is a basic structure to get you started. Modify it for your project!
"""

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

    print("\n" + "=" * 65)

def handle_choice(choice):
    """
    Process the user's choice and call appropriate functions.
    
    Args:
        choice (str): The user's input
        
    Returns:
        bool: True to continue, False to exit
    """
    if choice == "1":
        print("You chose option 1!")
        # TODO: Call your function here
        
    elif choice == "2":
        print("You chose option 2!")
        # TODO: Call your function here
        
    elif choice == "3":
        print("You chose option 3!")
        # TODO: Call your function here
        
    elif choice == "help":
        display_menu()
        
    elif choice == "quit":
        print("Thanks for using the application. Goodbye!")
        return False
        
    else:
        print(f"'{choice}' is not a valid option. Type 'help' to see available commands.")
    
    return True


def main():
    """
    Main application loop.
    Displays menu, gets user input, processes choices.
    """
    print("Welcome to the Console Application!")
    display_menu()
    
    running = True
    while running:
        choice = input("Enter your choice: ").strip().lower()
        running = handle_choice(choice)


if __name__ == "__main__":
    main()
