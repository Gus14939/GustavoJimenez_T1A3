import json
import os

from rich import print
from rich.console import Console
from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({
    "inp": "bold bright_white on #000000",
    "err": "bold bright_white on #9f1616"
})


from features import compute    

console = Console(theme=custom_theme)

# function to read json files
def read_json_data(json_file_name):
    with open(json_file_name, "r") as json_file:
        return json.load(json_file)

def find_file_with_suffix(directory, suffix):
    files = [f for f in os.listdir(directory) if f.endswith(suffix)]
    return files

def logged_in():
    directory_path = './'

    # Finding files with the "_active" suffix
    active_files = find_file_with_suffix(directory_path, '_active.json')

    # Return True if there's at least one active file
    return bool(active_files)

# Print MENU
def show_menu(menu_data):
    for category in menu_data["categories"]:
        console.print(f"\n{category['name']}:", style="bold #ca8610")
        for item in category["items"]:
            console.print(f" - [bold #f2e209 on black]{item['number']}[/] {item['name']}: [bold cyan]${item['price']:.2f}[/]")
    print()

    if logged_in():
        # for registered users only
        for category in menu_data["specials"]:
            console.print(f"\n[#f2e209]{category['name']}:[/]")
            for item in category["items"]:
                console.print(f" - [bold #f2e209]{item['number']}[/] [#ca8610]{item['name']}:[/] [bold #f2e209]${item['price']:.2f}[/]")
        print()

# User input
def select_item(menu_data):
    while True:
        try:
            menu_section_user_input = str(console.input("[inp]Select the [#f2e209]code[/] or type [green]'done'[/] to checkout:[/inp] ")).upper()

            # Check if the user wants to proceed to checkout
            if menu_section_user_input == "DONE":
                return None

            # Check if the user is logged in (has an active order)
            if logged_in():
                # Additional options for logged-in users
                for category in menu_data["specials"]:
                    for item in category["items"]:
                        if item["number"] == menu_section_user_input:
                            return item

            # Common menu options
            for category in menu_data["categories"]:
                for item in category["items"]:
                    if item["number"] == menu_section_user_input:
                        return item

            # Raise an error if the code is not found
            raise ValueError(f"Wrong code: {menu_section_user_input} is not in the menu")

        except ValueError as e:
            console.print(f"[bold]Error:[/] Invalid input. {e}", style="err")
            
def user_selected_item(selected_item):
    console.print(f"You have selected [#f2e209 on black]{selected_item['number']}[/] - {selected_item['name']} for a price of [bold cyan]$[/]{selected_item['price']:.2f}\n")

def create_user_order(menu_data):
    new_order = []
    while True:
        # select_item() function parameter menu_data
        selected_item = select_item(menu_data)
        if selected_item:
            user_selected_item(selected_item)
            new_order.append(selected_item)
        else:
            break

    with open("temp_user_order.json", "w") as json_file:
        json.dump(new_order, json_file, indent=2)
        """
        Write JSON data to a file.

        :param json_file_name: temp_user_order.json
        :param data: new_order = []
        """

# Print order
def show_order(order_data):
    total_price_order = sum(item['price'] for item in order_data)
    # total_prep_time = sum(item["prep_time"] for item in order_data)
    print()
    print("Here' is your order")
    print()
    console.print("[bold][#f2e209]{:<10}[/]{:<30}[cyan]{:<0}[/][/]".format('CODE ', 'ITEM', 'PRICE'))
    print()
    for item in order_data:
        console.print("[bold][#f2e209]{:<10}[/]{:<30}[cyan]${:<0.2f}[/][/]".format(item['number'], item['name'], item['price']))
    print()
    console.print("[bold][#f2e209]{:<10}[/]{:<30}[cyan]${:<0.2f}[/][/]".format('', 'TAKE-OUT TOTAL:', total_price_order))
    print()
    # print(total_prep_time)
    print()
    
def checkout(menu_data):
    console.print("Type in the [bold]'code'[/] and enter to remove")
    console.print("Type [bold #ca8610]'done'[/] to review your order")
    console.print("Type [bold #f2e209]'OK'[/] to finalize your order")
    print()
    while True:
        try:
            """
            Read JSON data from a file and return the loaded content.

            :param json_file_name: temp_user_order.json
            :return: Loaded JSON data.
            """
            read_order = read_json_data("temp_user_order.json")

            checkout_input = console.input("[inp]Code, done or OK:[/inp] ").upper()

            if checkout_input == "OK":
                break  # to exit the loop if the user types 'OK'
            elif checkout_input == "DONE":
                show_order(read_order)
                continue  # Continue the loop without checking further

            # Find the item with the matching code in the order
            item_to_remove = next((item for item in read_order if item['number'] == checkout_input), None)

            if item_to_remove:
                read_order.remove(item_to_remove)

                """
                Write JSON data to a file.

                :param json_file_name: temp_user_order.json
                :param data: item_to_remove
                """
                with open("temp_user_order.json", "w") as json_file:
                    json.dump(read_order, json_file, indent=2)                

                console.print(f"Item [err]{checkout_input} removed[/err] from the order.")
                print()
            else:
                raise ValueError(f"[u #cccccc]{checkout_input}[/] is not in your order")

        except ValueError as e:
            console.print(f"[bold]Invalid input:[/] {e}", style="err")

def processing_order():
    """
    Read JSON data from a file and return the loaded content.

    :param json_file_name: temp_user_order.json
    :return: Loaded JSON data.
    """
    read_order = read_json_data("temp_user_order.json")
    
    total_prep_time = sum(item["prep_time"] for item in read_order)
    compute(total_prep_time)
    
def find_single_file_with_suffix(directory, suffix):
    active_files = find_file_with_suffix(directory, suffix)
    if active_files:
        return os.path.join(directory, active_files[0])
    else:
        return None
# run_menu is the main func
def run_menu():
    
    print()
    console.print("Please choose by typing the [#f2e209]alpha-numeric [bold]code[/][/] from the menu")
    # show menu to the user
    menu_data = read_json_data("menu.json")
    show_menu(menu_data)

    # create user order
    create_user_order(menu_data)

    # print the order
    order_data = read_json_data("temp_user_order.json")
    show_order(order_data)

    # checkout - Modify or Ok order
    checkout(menu_data)

    # Time processing
    print()
    console.print("Your order is now COMPLETE!!", style="bold #ffeb3e on #9f1616")
    print()
    console.print("[#AAAAAA]We're [bold]preparing[/] your glorious meal[/]")
    console.print("It won't be long. [bold #f2e209]Here's the time to wait[/]")
    print()
    processing_order()
    
    # Delete the _active.json file
    active_file = find_single_file_with_suffix('./', '_active.json')
    if active_file:
        os.remove(active_file)
        # print(f"Deleted the {active_file} file.")

    # End of Journey
    print()
    console.print("Have a great day and come back soon", style="bold green")
    print("\n\n")

if __name__ == "__main__":
    run_menu()
