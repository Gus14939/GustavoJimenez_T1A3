# Self Ordering Kiosk // Gustavo Jimenez T1A3

import json
from register import run_register
from menu import run_menu
# from menu import 
# from checkout import
# from payment import 
# from features import compute
# from register import get_user_info

### REGISTRATION \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
# registration_selection()
# press 1 to register
# press 2 to log in
# press 3 to continue unregistered


# B-day !!!!

### MENU

# Show menu

# Take order

### CHECK-OUT

# Show receipt # if Remove # Show receipt

### PAYMENT

# Something simple match user imput to the total 

### END

def main():
    while True:
        print()
        print("WELCOME TO GUS' RESTAURANT!")

        run_register()
        run_menu()

        # to or quit
        user_input = input("press enter key to continue: ").lower()
        print()
        if user_input == 'quit':
            print("Goodbye!")
            break  # Exit the loop if the user enters 'q'

if __name__ == "__main__":
    main()