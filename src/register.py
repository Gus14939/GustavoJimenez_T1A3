
# import random
import json
import re
from rich import print
from rich.console import Console

console = Console()

# press 1 to register
def user_registration():
    print("\n\n")
    console.print("You'll have great perks after filling in this form. [#ca8610]Thanks for registering![/]")
    
    
    def create_user_code():
        """
        Read JSON data from a file and return the loaded content.

        :param json_file_name: user_database.json
        :return: Loaded JSON read_data.
        """
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
                if not get_user_info["name"]:
                    raise ValueError("Name cannot be empty.")
            except ValueError as e:
                console.print(f"Error: {e}", style="red")
            else:
                break
        while True:
            try:
                get_user_info["birthday"] = input("and your Bday (YYYY-MM-DD): ")
                if not Bday_format_valid(get_user_info["birthday"]):
                    raise ValueError("Invalid format, please try YYYY-MM-DD")
            except ValueError as e:
                console.print(f"Error: {e}", style="red")
            else:
                break
        get_user_info["user_code"] = personal_user_code
        # Create file
        new_user_database_file_name = f"user_{get_user_info['user_code']}_active.json"        
        create_user_json_file(new_user_database_file_name, get_user_info)  
        
        print()
        console.print(f"Welcome [bold green]{get_user_info['name']}[/]")
        console.print(f"Your personal code is {get_user_info['user_code']}. [yellow]Don't loose it![/]")
        console.print("Use this [yellow on black]code every[/] time you comeback for added value and gifts!")
        return get_user_info
        

        # file_name = (f"{get_user_info['name']}_{get_user_info['user_code']}_new_user.json")

    def save_user_to_db(new_user_to_db):
        """
        Read JSON data from a file and return the loaded content.

        :param json_file_name: user_database.json
        :return: Loaded JSON current_user_db.
        """    
        with open("user_database.json", "r") as json_file:
            current_user_db = json.load(json_file)
        
        # append new user
        current_user_db.setdefault("registered_users", []).append(new_user_to_db)

        """
        Write JSON data to a file.

        :param json_file_name: user_database.json
        :param data: current_user_db
        """
        with open("user_database.json", "w") as json_file:
            json.dump(current_user_db, json_file, indent=2 ) 
    
    new_user_to_db = get_new_user_info()
            
    save_user_to_db(new_user_to_db)

#
def create_user_json_file(file_name, data):
    
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# press 2 to log in
def user_login():
    counter = 0
    while counter < 3:            
        try:                
            # User input
            get_user_code = input("What is your 3-number-code: ")
            
            # Error Handling
            if not get_user_code:
                raise ValueError("Should not be empty.")
            
            if len(get_user_code) != 3:
                raise ValueError("Please enter a 3-digit number")

            if not get_user_code.isdigit():
                raise TypeError("Please enter only numbers")

            get_user_code = int(get_user_code)

            """
            Read JSON data from a file and return the loaded content.

            :param json_file_name: user_database.json
            :return: Loaded JSON user_database.
            """    
            with open("user_database.json", "r") as json_file:
                user_database = json.load(json_file)
            
            users_in_database = user_database["registered_users"]
            
            user_registered_db = next((user for user in users_in_database if user["user_code"] == get_user_code), None)
            
            if user_registered_db:
                print()
                console.print(f"[bold green]Hi {user_registered_db['name']}[/], welcome back!")
                # Create the individual user database
                # new user login database create name
                new_user_personal_database = user_registered_db
                new_user_database_file_name = f"user_{user_registered_db['user_code']}_active.json"
                
                """
                Write JSON data to a file.

                :param json_file_name: new_user_database_file_name - user_'user-code'_active.json
                :param data: new_user_personal_database
                """
                create_user_json_file(new_user_database_file_name, new_user_personal_database)    
                    
                # not sure if this is returning what I want!    
                return user_registered_db
            else:
                raise ValueError("User not found in the database.")
                # return None
                
        except ValueError as e:
            console.print(f"[bold red]Error:[/] {e}")
        except TypeError as e:
            console.print(f"[bold red]Error:[/] {e}")
        else:
            break
        counter += 1
        # Number of tries
        if counter == 1:
            print("You have 2 more tries")
        if counter == 2:
            print("You have 1 more triy")
    else:
        # Code recovery process
        print()
        console.print("You have exceeded the maximum number of attempts. Let's recover your account.")
        registration_retrieve()


# account recovery
def registration_retrieve():
    print()
    print(("Code number recovery").upper())
    print()
    print("Tell us your Name and Birthday")
    print()
    # Catch birthday correctly
    def Bday_format_valid(date_str):
        date_format = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        return bool(date_format.match(date_str))
    ## retrive code
    get_user_info = {}
    while True:
        try:
            get_user_info["name"] = input("What is your name: ").capitalize()
            if any(char.isdigit() for char in get_user_info["name"] ):
                raise ValueError("Please enter valid name, no numbers.")
            if not get_user_info["name"]:
                raise ValueError("Name cannot be empty.")
        except ValueError as e:
            console.print(f"Error: {e}", style="red")
        else:
            break
    while True:
        try:
            get_user_info["birthday"] = input("and your Bday (YYYY-MM-DD): ")
            if not Bday_format_valid(get_user_info["birthday"]):
                raise ValueError("Invalid format, please try YYYY-MM-DD")
        except ValueError as e:
            console.print(f"Error: {e}", style="red")
        else:
            break
    
    with open("user_database.json", "r") as json_file:
        read_data = json.load(json_file)    
        
    does_user_exists = read_data.get("registered_users", [])
    
    # print("Contents of does_user_exists:")
    # for user in does_user_exists:
    #     print(user)
    
    idiot_user = [user for user in does_user_exists if user.get("name") == get_user_info["name"] and user.get("birthday") == get_user_info["birthday"]]

    if idiot_user:
        idiot_user = idiot_user[0]  # Retrieve the first (and only) user from the list
        print()
        print(f"Hi {idiot_user['name']} Here is your code {idiot_user['user_code']}")
        print()
        run_register()
    else:
        print()
        console.print("User not found. Register or try step 2 again please check your name and birthday.", style="bold  #CA8610 on red")
        run_register()

         

# press 3 to continue unregistered
def user_unregistered():
    print()
    console.print("[bold #ca8610]Hello Stranger,[/] welcome to Gus' restaurant")
    return None

# 1st function in run_     
def registration_selection():
    print()
    console.print("Select from the 3 options below", style="bold")
    print()
    
    console.print("[bold]Type 1[/] to [bold cyan]Register[/] to Gus' Restaurant")
    console.print("[bold]Type 2[/] to Login with your [bold cyan]code number[/]")
    console.print("[bold]Type 3[/] to continue as a [bold #ca8610]Visitor[/]")
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
            console.print(f"Error: {e}", style="red")
    


if __name__ == "__main__":
    run_register()
