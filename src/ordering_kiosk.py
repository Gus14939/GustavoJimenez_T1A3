# Self Ordering Kiosk // Gustavo Jimenez T1A3
import json
from register import run_register
from menu import run_menu
from rich import print
from rich.console import Console

console = Console()

def main():
    while True:
        print()
        console.print("WELCOME TO GUS' RESTAURANT!", style="bold #ca8610 on red")

        run_register()
        run_menu()

        # to or quit
        user_input = console.input("press [bold green]enter key[/] to continue: ").lower()
        print()
        if user_input == 'quit':
            console.print("[bold red]Goodbye![/]")
            print()
            break  # Exit the loop if the user enters 'q'

if __name__ == "__main__":
    main()