
# import random
import json
import re
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
    
    # Catch birthday correctly
    def Bday_format_valid(date_str):
        date_format = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        return bool(date_format.match(date_str))
    
    def get_new_user_info():
        get_user_info = {}
        while True:
            try:
                get_user_info["name"] = input("What is your name: ").capitalize()
                if any(char.isdigit() for char in get_user_info["name"] ):
                    raise ValueError("Please enter valid name, no numbers.")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                break
        while True:
            try:
                get_user_info["birthday"] = input("and your Bday (YYYY-MM-DD): ")
                if not Bday_format_valid(get_user_info["birthday"]):
                    raise ValueError("Invalid format, please try YYYY-MM-DD")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                break
        get_user_info["user_code"] = personal_user_code
        print()
        print(f"Welcome {get_user_info['name']}")
        print(f"Your personal code is {get_user_info['user_code']}. Don't loose it!")
        print("Use this code every time you comeback for added value and gifts!")
        return get_user_info
        

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
    while True:
        try:
            get_user_code = input("What is your 3-number-code: ")
            
            if len(get_user_code) != 3:
                raise ValueError("Please enter a 3-digit number")

            if not get_user_code.isdigit():
                raise TypeError("Please enter only numbers")

        except ValueError as e:
            print(f"Error: Invalid input. {e}")
        except TypeError as e:
            print(f"Error: {e}")
        else:
            break
        
    # Move the conversion to int inside the try block to handle valid input
    
    get_user_code = int(get_user_code)

    # Read the user database
    with open("user_database.json", "r") as json_file:
        user_database = json.load(json_file)
    
    users_in_database = user_database["registered_users"]
    
    user_registered_db = next((user for user in users_in_database if user["user_code"] == get_user_code), None)

    if user_registered_db:
        print()
        print(f"Hi {user_registered_db['name']}, welcome back!")
    else:
        print("User not found in the database.")
    


# press 3 to continue unregistered
def user_unregistered():
    print()
    print("Hello Stranger, welcome to Gus' restaurant")
    return None
            
def registration_selection():
    print()
    print("Select from the 3 options below")
    print()
    
    print("Type 1 to Register to Gus' Restaurant")
    print("Type 2 to Login with your code number")
    print("Type 3 to continue un-registered")
    print()

user_choice = ""

# press 1 to register
# press 2 to log in
# press 3 to continue unregistered

# registration_selection()
   
def run_register():
    
    registration_selection()
    while True:
        try:
            user_choice = input("How would you like to proceed?: ")
            if not user_choice.isdigit():
                raise ValueError("Please enter a valid number.")
            user_choice = int(user_choice)  # Convert user input to integer

            if user_choice == 1:
                user_registration()
            elif user_choice == 2:
                user_login()
            elif user_choice == 3:
                user_unregistered()
            else:
                raise ValueError("Type 1, 2, or 3, please")
            break

        except ValueError as e:
            print(f"Error: {e}")
    


if __name__ == "__main__":
    run_register()
