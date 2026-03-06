import quiz_engine
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.rule import Rule
from rich.prompt import Prompt
from rich.theme import Theme

LOTR_FILE = "data/lotr.json"
DARK_SOULS_FILE = "data/dark_souls.json"

theme = Theme(
    {
        "title": "bold cyan",
        "gold": "bold yellow",
        "bonfire": "bold red",
        "good": "bold green",
        "bad": "bold red",
        "muted": "dim white",
        "cmd": "bold yellow",
        "accent": "bold magenta",
    }
)

console = Console(theme=theme)


ASCII_TITLE = r"""
   ██████╗ ██╗   ██╗██╗███████╗
  ██╔═══██╗██║   ██║██║╚══███╔╝
  ██║   ██║██║   ██║██║  ███╔╝
  ██║▄▄ ██║██║   ██║██║ ███╔╝
  ╚██████╔╝╚██████╔╝██║███████╗
   ╚══▀▀═╝╚═╝╚═════╝ ╚═╝╚══════╝
""".rstrip("\n")


def build_menu_panel() -> Panel:
    title = Text()
    title.append(ASCII_TITLE + "\n", style="title")
    title.append("The Perfect Python Quiz for Fans\n", style="gold")
    title.append("⛧   Created by Caleb and E  ⛧\n", style="bonfire")

    body = Text()
    body.append("\nChoose your challenge:\n\n", style="muted")
    body.append("  1) ⚔️  The One Ring Trial  — Lord of the Rings\n", style="good")
    body.append("  2) 🔥  Kindle the Flame    — Dark Souls\n", style="bonfire")
    body.append("  3) 📜  Lore Mode (stretch goal)\n", style="title")

    body.append("\n", style="muted")
    body.append("  help  - Show help\n", style="cmd")
    body.append("  quit  - Exit the quiz\n", style="cmd")

    content = Align.center(title + body)

    return Panel(
        content,
        border_style="gold",
        padding=(1, 2),
        title="[gold]QUIZ MENU[/gold]",
        subtitle="[muted]Type 1 / 2 / 3 / help / quit[/muted]",
    )


def show_menu():
    console.clear()
    console.print(build_menu_panel())
    console.print(Rule(style="muted"))


def show_help():
    console.clear()
    help_text = Text()
    help_text.append("Help / Commands\n", style="title")
    help_text.append("\n", style="muted")
    help_text.append("• ", style="muted")
    help_text.append("1", style="good")
    help_text.append("  — Start Lord of the Rings quiz\n", style="muted")

    help_text.append("• ", style="muted")
    help_text.append("2", style="bonfire")
    help_text.append("  — Start Dark Souls quiz\n", style="muted")

    help_text.append("• ", style="muted")
    help_text.append("3", style="title")
    help_text.append("  — Lore Mode (coming soon)\n", style="muted")

    help_text.append("• ", style="muted")
    help_text.append("help", style="cmd")
    help_text.append(" — Show this help page\n", style="muted")

    help_text.append("• ", style="muted")
    help_text.append("quit", style="cmd")
    help_text.append(" — Exit the program\n", style="muted")

    help_text.append("\nTips:\n", style="accent")
    help_text.append("• If your quiz supports it, type 'quit' during a question to exit early.\n", style="muted")

    console.print(
        Panel(
            help_text,
            border_style="title",
            padding=(1, 2),
            title="[title]HELP[/title]",
        )
    )
    console.print()
    input("Press Enter to return to the bonfire...")


def handle_choice(choice: str) -> bool:
    if choice == "1":
        console.print("[good]⚔️  Summoning the Fellowship...[/good]")
        quiz_engine.run_quiz(LOTR_FILE)
        input("\nPress Enter to return to the bonfire...")
        return True

    if choice == "2":
        console.print("[bonfire]🔥  Kindling the First Flame...[/bonfire]")
        quiz_engine.run_quiz(DARK_SOULS_FILE)
        input("\nPress Enter to return to the bonfire...")
        return True

    if choice == "3":
        console.print("[title]📜 Lore Mode coming soon (stretch goal).[/title]")
        input("\nPress Enter to return to the bonfire...")
        return True

    if choice == "help":
        show_help()
        return True

    if choice == "quit":
        console.print("[gold]Thanks for playing.[/gold] [muted]May your code compile on the first try.[/muted]")
        return False

    console.print(f"[bad]'{choice}' is not a valid option.[/bad] [muted]Type[/muted] [cmd]help[/cmd] [muted]to see commands.[/muted]")
    return True


def main():
  try:
        running = True
        while running:
            show_menu()
            try:
                choice = Prompt.ask(
                    "[title]Enter your choice[/title] [muted](1/2/3/help/quit)[/muted]",
                    default="help"
                ).strip().lower()
            except (KeyboardInterrupt, EOFError):
                console.print("\n[gold]Thanks for playing.[/gold] [muted](goodbye!)[/muted]")
                return

            running = handle_choice(choice)

  except KeyboardInterrupt:
        # If Ctrl+C happens anywhere else (like inside quiz_engine)
        console.print("\n[gold]Thanks for playing.[/gold] [muted](goodbye!)[/muted]")


if __name__ == "__main__":
    main()