# while True:
#     try:
#         get_user_code = int(input("What is your 3-number-code: "))

#         if not (100 <= get_user_code <= 999):
#             raise ValueError("Please enter a 3-digit number")
#     except ValueError as e:
#         print(f"Error: Invalid input. {e}")
#         # Add custom error message for non-integer input
#         if "invalid literal for int() with base 10" in str(e):
#             print("Error: Please enter only numeric values.")
#     else:
#         break

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
    # finally:
        # get_user_code

print(type(get_user_code))
get_user_code = int(get_user_code)  
print(type(get_user_code))


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
    try:
        get_user_code = int(get_user_code)
    except ValueError as e:
        print(f"Error converting to integer: {e}")
        return  # or handle the error appropriately

    # Read the user database
    with open("user_database.json", "r") as json_file:
        user_database = json.load(json_file)
    
    users_in_database = user_database["registered_users"]
    
    # Iterate through users and print their user codes
    for user in users_in_database:
        print(user["user_code"])