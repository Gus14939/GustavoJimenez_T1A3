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

Copy code
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

order_data = [
    {'number': 1, 'name': 'Item 1', 'price': 10.50},
    {'number': 2, 'name': 'Item 2', 'price': 20.75},
    {'number': 3, 'name': 'Item 3', 'price': 15.00},
]

text_lines = []

for item in order_data:
    text_lines.append(
        "[bold][yellow]{:<10}[/]{:<30}[cyan]${:<0.2f}[/][/]".format(item['number'], item['name'], item['price'])
    )

# Join all text lines into a single Text object
text = Text('\n'.join(text_lines))

# Calculate the width and height based on the content size
width = max(len(line) for line in text.plain.split('\n')) + 4  # Adding some padding
height = text.plain.count('\n') + 4  # Adding some padding

# Create a single panel for all items
panel = Panel(text, title="YOUR ORDER", width=width, height=height)

console.print(panel)