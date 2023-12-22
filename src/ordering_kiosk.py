# Self Ordering Kiosk // Gustavo Jimenez T1A3
from rich import print
from rich.console import Console

from register import run_register
from menu import run_menu

console = Console()

def main():
    while True:
        print()
        console.print("WELCOME TO GUS' RESTAURANT!", style="bold #ffeb3e on red")

        run_register()
        run_menu()

        # to or quit
        user_input = console.input("press [bold green]enter key[/] to make another order or [bold red]type quit[/] to finish: ").lower()
        print()
        if user_input == 'quit':
            console.print("[bold red]Goodbye![/]")
            print()
            break  # Exit the loop if the user enters 'quit'
        
if __name__ == "__main__":
    main()