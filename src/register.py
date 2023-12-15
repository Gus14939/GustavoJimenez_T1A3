
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
# press 1 to register
def user_registration():
    print("\n\n")
    print("You'll have great perks after filling in this form. Thanks for registering!")
    
    
    def create_user_code():
        with open("user_database.json", "r") as json_file:
            read_data = json.load(json_file)
        
        registered_users = read_data.get("registered_users", [])
        
        if registered_users:
            last_user = max(users["user_code"] for users in registered_users)   
            new_user_code = last_user + 1
        else:
            new_user_code = 100
        
        return new_user_code
                
        # return random.randint(100, 120)        
    personal_user_code = create_user_code()
    
    def get_new_user_info():
        get_user_info = {}
        get_user_info["name"] = str(input("What is your name: ")).capitalize()
        get_user_info["Birthday"] = input("and your Bday (YYYY-MM-DD): ")
        get_user_info["user_code"] = personal_user_code
        return get_user_info
        
        print(f"Welcome {get_user_info['name']}, your personal code is {get_user_info['user_code']}. Don't loose it")

        # file_name = (f"{get_user_info['name']}_{get_user_info['user_code']}_new_user.json")

    def save_user_to_db(new_user_to_db):
    #read json
        with open("user_database.json", "r") as json_file:
            current_user_db = json.load(json_file)
    # append new user
        current_user_db.setdefault("registered_users", []).append(new_user_to_db)
    # write to db json
        with open("user_database.json", "w") as json_file:
            json.dump(current_user_db, json_file, indent=2 ) 
    
    new_user_to_db = get_new_user_info()
            
    save_user_to_db(new_user_to_db)
    
# press 2 to log in
def user_login():
    get_user_code = int(input("What is your 3 number code: "))

    with open("user_database.json", "r") as json_file:
        user_database = json.load(json_file)
    
    users_in_database = user_database["registered_users"]
    
    for user in users_in_database:
        if user["user_code"] == get_user_code:
            print("\n\n")
            print(f"Hi {user['name']}, welcome back!")
            print("Plase choose by typing the alpha-numeric code from our menu below")
            
        
# press 3 to continue unregistered
def user_unregistered():
    print("\n\n")
    print("Hello Stranger, welcome to Gus' restaurant")
    print("Plase choose by typing the alpha-numeric code from our menu below")
    return None
            
def registration_selection():
    print("\n\n")
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
        


if __name__ == "__main__":
    run_register()