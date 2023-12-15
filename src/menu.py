from features import compute
import json

print()
print("GUS' RESTAURANT MENU")

def read_menu():
    with open("menu.json", "r") as json_file:
        return json.load(json_file)

# Print MENU
def show_menu(menu_data):
    for category in menu_data["categories"]:
        print(f"\n{category['name']}:")
        for item in category["items"]:
            print(f" - {item['number']} {item['name']}: ${item['price']:.2f} - {item['prep_time']}")
    print()

# User input
def select_item(menu_data):
    user_to_select_item = str(input("Select the number of your food or type 'done' to finish: ")).upper()
    if user_to_select_item == "DONE":
        return None
    for category in menu_data["categories"]:
        for item in category["items"]:
            if item["number"] == user_to_select_item:
                return item
    return None

def user_selected_item(selected_item):
    print(f"You have selected {selected_item['number']} - {selected_item['name']} for a price of ${selected_item['price']:.2f}\n")
    # selected_item_prep_time = selected_item['prep_time']
    # from features_mocks TIME - prep_time
    # compute(selected_item_prep_time)

def print_menu(menu_data):
    show_menu(menu_data)

def run_menu():
    menu_data = read_menu()
    print_menu(menu_data)
    order = []
    while True:
        selected_item = select_item(menu_data)
        if selected_item:
            user_selected_item(selected_item)
            order.append(selected_item)
        else:
            break

    # Process the completed order or perform any necessary actions
    print("Order complete. Processing order...")
    # Example: Compute the total time for the order
    print(f"Take-Out total:  ${sum(item['price'] for item in order):.2f}")
    total_time = sum(item['prep_time'] for item in order)
    compute(total_time)



run_menu()