from features import compute
import json

print()
print("Plase choose by typing the alpha-numeric code from our menu below")


def read_json_data(json_file_name):
    with open(json_file_name, "r") as json_file:
        return json.load(json_file)

# Print MENU
def show_menu(menu_data):
    for category in menu_data["categories"]:
        print(f"\n{category['name']}:")
        for item in category["items"]:
            print(f" - {item['number']} {item['name']}: ${item['price']:.2f} - {item['prep_time']}")
    print()

# Print order
def show_order(order_data):
    total_price_order = sum(item['price'] for item in order_data)
    total_prep_time = sum(item["prep_time"] for item in order_data)
    print()
    print("Here' is your order")
    print()
    print("{:<10}{:<30}{:<0}".format('CODE ', 'ITEM', 'PRICE'))
    for item in order_data:
        print("{:<10}{:<30}${:<0.2f}".format(item['number'], item['name'], item['price']))
    print()
    print("{:<10}{:<30}${:<0.2f}".format( ' ', 'Take-Out total:', total_price_order ).upper())
    print()
    print(total_prep_time)
    # print(f"Take-Out total:  ${sum(item['price'] for item in order_data):.2f}")
    
    print()
    
# User input
def select_item(menu_data):
    menu_section_user_input = str(input("Select the code or type 'done' to checkout: ")).upper()
    if menu_section_user_input == "DONE":
        return None
    for category in menu_data["categories"]:
        for item in category["items"]:
            if item["number"] == menu_section_user_input:
                return item
    # return None

def user_selected_item(selected_item):
    print(f"You have selected {selected_item['number']} - {selected_item['name']} for a price of ${selected_item['price']:.2f}\n")


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
        
    # total_time = sum(item['prep_time'] for item in new_order)
    # compute(total_time)

# Remove from order=
def checkout(menu_data): #remove_order_data):
    while True:
        read_order = read_json_data("temp_user_order.json")
        
        print("Type in the 'code' and enter to remove")
        print("Type 'done' to review your order")
        print("Type 'OK' to finalize your order")
        print()
        
        checkout_input = input("Code(s) and done or OK: ").upper()
        
        if checkout_input == "OK":
            break  # to exit the loop if the user types 'OK'
        elif checkout_input == "DONE":
            show_order(read_order)

        # Find the item with the matching code in the order
        item_to_remove = next((item for item in read_order if item['number'] == checkout_input), None)
        
        if item_to_remove:
            read_order.remove(item_to_remove)
            
            # Update the temp_user_order.json file with the modified order
            with o1pen("temp_user_order.json", "w") as json_file:
                json.dump(read_order, json_file, indent=2)
            
            print(f"Item {checkout_input} removed from the order.")
        else:
            print(f"No item found with code {checkout_input} in the order.")

def processing_order():
    read_order = read_json_data("temp_user_order.json")
    total_prep_time = sum(item["prep_time"] for item in read_order)
    compute(total_prep_time)
    

# run_menu is the main func
def run_menu():
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
    processing_order()
    print("Order complete. Processing order...")

    # End of Journey
    print("\n\n")
    print("Have a great day and come back soon")
    print("\n\n")
    
    # Example: Compute the total time for the order
    # print(f"Take-Out total:  ${sum(item['price'] for item in order):.2f}")
    # compute(total_time)


if __name__ == "__main__":
    run_menu()