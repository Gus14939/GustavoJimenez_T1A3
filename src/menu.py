from features import compute
import json

print()
print("GUS' RESTAURANT MENU")

def read_data(json_file_name):
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
    print()
    print("Here' is your order")
    print()
    print("{:<10}{:<30}{:<0}".format('CODE ', 'ITEM', 'PRICE'))
    for item in order_data:
        print("{:<10}{:<30}${:<0.2f}".format(item['number'], item['name'], item['price']))
    print()
    print("{:<10}{:<30}${:<0.2f}".format( ' ', 'Take-Out total:', total_price_order ).upper())
    # print(f"Take-Out total:  ${sum(item['price'] for item in order_data):.2f}")
    
    print()
    
# Remove from order=
def checkout_order(remove_order_data): #remove_order_data):
    
    read_order = read_data("temp_user_order.json")
    print(read_order)
    
    for item in read_order:
        return item['number']
    
    print("type OK if you wish to proceed to payment, or")
    print("type the code of the item you wish to remove")
    
    
    while True:
        selected_item = select_item(menu_data)
        if selected_item:
            user_selected_item(selected_item)
            order.append(selected_item)
        else:
            break
        
    checkout_input = input("type OK or the code: ").upper()
    
    if checkout_input == "OK":
        return None
    elif checkout_input == item['number']:
        # for item in remove_order_data:
        pass
    #     item['number'], item['name'], item['price']

# User input
def select_item(menu_data):
    menu_section_user_input = str(input("Select the number of your food or type 'done' to finish: ")).upper()
    if menu_section_user_input == "DONE":
        return None
    for category in menu_data["categories"]:
        for item in category["items"]:
            if item["number"] == menu_section_user_input:
                return item
    # return None

def user_selected_item(selected_item):
    print(f"You have selected {selected_item['number']} - {selected_item['name']} for a price of ${selected_item['price']:.2f}\n")
    # selected_item_prep_time = selected_item['prep_time']
    # from features_mocks TIME - prep_time
    # compute(selected_item_prep_time)

def print_menu(menu_data):
    show_menu(menu_data)

def print_order(order_data):
    show_order(order_data)
    
def checkout(remove_order_data):
    checkout_order(remove_order_data)
    

def run_menu():
    menu_data = read_data("menu.json")
    print_menu(menu_data)
    
    
    order = []
    while True:
        # select_item() function parameter menu_data
        selected_item = select_item(menu_data)
        if selected_item:
            user_selected_item(selected_item)
            order.append(selected_item)
        else:
            break
    
    with open("temp_user_order.json", "w") as json_file:
        json.dump(order, json_file, indent=2)    
    
    order_data = read_data("temp_user_order.json")
    print_order(order_data)
    
    # checkout()

 
    print("Order complete. Processing order...")
    # Example: Compute the total time for the order
    # print(f"Take-Out total:  ${sum(item['price'] for item in order):.2f}")
    
    print()
    print()
    print()
    total_time = sum(item['prep_time'] for item in order)
    compute(total_time)


if __name__ == "__main__":
    run_menu()