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
    print()
    print("Welcome to Gus' restaurant!\nLet's get started with your registration.")

    run_register()
    run_menu()

if __name__ == "__main__":
    main()