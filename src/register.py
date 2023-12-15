
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

def user_registration():
    print()
    print("You'll have great perks after filling in this form. Thanks for registering!")
    
    def create_user_code():
        return random.randint(100, 120)            
    personal_user_code = create_user_code()

    get_user_info = {}
    get_user_info["name"] = str(input("What is your name: "))
    get_user_info["Birthday"] = input("and your Bday (YYYY-MM-DD): ")
    get_user_info["user_code"] = personal_user_code
    
    print(f"Welcome {get_user_info['name']}, your personal code is {get_user_info['user_code']}. Don't loose it")


    file_name = (f"{get_user_info['name']}_{get_user_info['user_code']}_new_user.json")

    def save_user_info():
        with open(file_name, "w") as json_file:
            json.dump(get_user_info, json_file)
            
    save_user_info()

def user_login():
    get_user_code = int(input("What is your 3 number code: "))
    
    with open("user_database.json", "r") as json_file:
        user_database = json.load(json_file)
    
    users_in_database = user_database["registered_users"]
    
    for user in users_in_database:
        if user["user_code"] == get_user_code:
            print(f"hi {user['name']}")
        
def user_unregistered():
    return None
            
def registration_selection():    
    print("Select from the 3 options below")
    print()
    
    print("Type 1 to Register to Gus' Restaurant")
    print("Type 2 to Login with your code number")
    print("Type 3 to continue un-registered")
    print()
    
    choice = int(input("How would you like to proceed?: "))
    return choice

user_choice = ""

# press 1 to register
# press 2 to log in
# press 3 to continue unregistered

# registration_selection()
   
def run_register():
    user_choice= registration_selection()   
    if user_choice == 1:
        user_registration()
    elif user_choice == 2:
        user_login()
    else:
        user_unregistered()
        

run_register()