
'''
Implement user registration with name, birthday, and a unique 3-number code

1. Collect User Information:
   - Prompt the user to enter their name and birthday.
   - store it

2. Generate a Unique Code:
   - Generate a unique 3-number code? 

3. Store User Information:
   - Store the user information, including the name, birthday, and unique code. 
   This could be a dictionary
   a Json file to keep the data.

4. Offer Discounts and Birthday Offers:
   - Implement logic to check if it's the user'sB-day
   birthday offers based on their info.

'''
import random
import json

list_of_user_numbers_created = []

def create_user_code():
    return random.randint(100, 120)
    
    
personal_user_code = create_user_code()

print(personal_user_code)

import json
get_user_info = {}
get_user_info["name"] = str(input("What is your name: "))
get_user_info["Birthday"] = input("and your Bday (YYYY-MM-DD): ")
get_user_info["user_code"] = personal_user_code


file_name = (f"{get_user_info['name']}_{get_user_info['user_code']}_new_user.json")

def save_user_info():
    with open(file_name, "w") as json_file:
        json.dump(get_user_info, json_file)
        
save_user_info()
'''


# Get user input
user_data = {}
user_data["name"] = input("Enter your name: ")
user_data["age"] = int(input("Enter your age: "))
user_data["city"] = input("Enter your city: ")

# Specify the file name
file_name = (f"{user_data['name']}.json")

# Write the user data to the JSON file
with open(file_name, "w") as json_file:
    json.dump(user_data, json_file)

print(f"The JSON file '{file_name}' has been created with your data.")
'''