#    python3 -m venv .kiosk
#     source .kiosk/bin/activate    
#     pip3 freeze>requirements.txt

from rich import print
from rich.console import Console

console = Console()


console.print("This is some text.")
console.print("This is some text.", style="bold")
console.print("This is some text.", style="bold underline")
console.print("This is some text.", style="bold underline green")
console.print("This is some text.", style="bold underline red on white")

console.print("[bold]This is [cyan]some text.[/] bold underline red on white[/]")



print(f"Let's do some math: 2 + 2 = {2 + 2}")
print({"a": [1, 2, 3], "b":{"c":5}})

from rich.text import Text

text =Text("wasss upppp yo")
text.stylize("bold magenta", 0, 5)
console.print(text)

from rich import print
from rich.panel import Panel
from rich.text import Text
panel = Panel(Text("Hello", justify="right"))
print(panel)