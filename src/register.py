
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
'''
import json

file_name = get_user_info

def get_user_info():
    with open(file_name, "w") as json_file:
        json.dump(user_info_input)

'''

import json

# Get user input
user_data = {}
user_data["name"] = input("Enter your name: ")
user_data["age"] = int(input("Enter your age: "))
user_data["city"] = input("Enter your city: ")

# Specify the file name
file_name = "user_data.json"

# Write the user data to the JSON file
with open(file_name, "w") as json_file:
    json.dump(user_data, json_file)

print(f"The JSON file '{file_name}' has been created with your data.")