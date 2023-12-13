import json

# Read MENU json file
with open("menu.json", "r") as json_file:
    data_MENU_read = json.load(json_file)
# print(data_MENU_read)

# Print MENU
for category in data_MENU_read["categories"]:
    print(f"\n{category['name']}:")
    for item in category["items"]:
        print(f"  - {item['number']} {item['name']}: ${item['price']:.2f}")
print()
#

# User input
user_to_select_item = input("Select the number of your food: ")

for category in data_MENU_read["categories"]:
    for item in category["items"]:
        if item["number"] == user_to_select_item:
            print("SELECTED")
            selected_item = item
            #print(type(selected_item))
            break


def user_selected_item():
    print(f"you have selected {selected_item['number']} - {selected_item['name']} for a price of ${selected_item['price']:.2f}\n")
    

user_selected_item()

