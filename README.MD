# Gustavo Jimenez T1A3 - Self Service Kiosk
  
### R1. Answers to all the documentation requirements below.
### R2. Your README.md should have a separate heading for each documentation requirement and answers organised under the appropriate headings.

### R3. Provide full attribution to referenced sources (where applicable).
rich library ---- https://www.youtube.com/watch?v=4zbehnz-8QU
    https://rich.readthedocs.io/en/latest/index.html

alive-progress library --- https://pypi.org/project/alive-progress/
    https://pypi.org/project/alive-progress/

json files --- https://www.pythoncheatsheet.org/cheatsheet/json-yaml

### R4. Provide a link to your source control repository
 - ### [GustavoJimenez_T1A3-GitProject](https://github.com/Gus14939/GustavoJimenez_T1A3)
    
### R5. Identify any code style guide or styling conventions that the application will adhere to.  
Reference the chosen style guide appropriately.

**The code is well-organized and follows PEP 8 and PEP 257 conventions. Here are a few points I kept in mind:**
 
 - Imports: Kept them at the top, but re-organised and grouped appropriately.

 - Whitespace: use of whitespace is maintained around operators and after commas.

 - Indentation: The code is consistently indented using 4 spaces per level.

 - String Formatting: F-strings are used for string formatting, which is more concise and readable.
    - Some string were not F-string for personal readability 

 - Comments/Docstrings: Applied informative comments, I used triple double-quotes.

 - Function Documentation: Functions have docstrings describing their purpose, parameters, and return values.

 - Variable Names: Variable names are descriptive, and there are no formats inconsistencies.

 - Consistent Case format: Snake case for both variable and function names.

### R6. Develop a list of features that will be included in the application. It must include:

- at least THREE features
- describe each feature

    Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:

    - use of variables and the concept of variable scope
    - loops and conditional control structures
    - error handling

Consult with your educator to check your features are sufficient .

#### User-friendly interface:  
The interface should be easy to navigate and understand, with clear instructions and options for the user. Displaying the menu in a clear and organised manner, with categories and prices for each item.

#### Create user registration, user login, login password recovery, and continue as visitor
- Allowing and encouraging users to register to have access to special products on the menu and other perks. 
- Password and login to access the specials and have a personal database
- Password recovery, if the user forgot the code, this can be retrieved by providing name and birthday.
- A simple continue as visitor or first time buyer

#### User Order tracking:  
Providing users with personal database to provide special products, customised orders, provide discounts.

#### Order display and remove items:  
Allowing users to add and preview the order. Remove unwanted items, preview and continue with purchase

#### Order Finalization:  
After the user has reviewed their order, the kiosk should confirm the order and display a message with an estimated wait time. It should also provide a receipt with the order details and total cost.

#### Order time to prepare:
Allowing users to see the time it will take and a progress bar indicating when the meal would be ready


Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:
    - use of variables and the concept of variable scope
    - loops and conditional control structures
    - error handling

- Consult with your educator to check your features are sufficient.

    ### [My Wireframe/Diagram](https://drive.google.com/file/d/1L3Ua_SGRIWJWtKAxmnS1D9oPsWyiOnRA/view?usp=sharing)

### R7. Develop an implementation plan which:

---  
**Set Up Project Structure:**

Create a new Python project directory.  
Set up version control (e.g., Git) for your project.  
Create Initial Files:
- Create a main Python script (e.g., ordering_kiosk.py) to serve as the entry point for your application.

- Create a menu file (e.g., menu.json) to store your menu items.

**Implement Menu Display**

- Read the menu data from menu.json in your main script.

- Implement a function to display the menu with item numbers, categories, and prices.

- Test the menu display functionality.

**Implement Order Placement:**

- Implement a function to handle order placement, allowing users to add items to their order by entering item numbers and quantities.

- Test order placement functionality.

**Implement Optional Features / Test / Debug**
1. Implement Order Summary:

    - Create a data structure to store the user's order.

    - Implement a function to display a summary of the user's order, including item names, quantities, and total cost.

    - Test the order summary functionality.

2. Implement Order Finalization:

    - Implement a function to confirm the order, display an estimated wait time, and provide a receipt with order details and total cost.

    - Test the order finalization functionality.

**Implement Error handling:**  
Implement error handling for invalid input and items.
    - Register page - user register error handling
    - Register page - user login error handling and 3-try-limit
    - Register page - continue as a visitor error handling



---


### [Link to my project in Trello](https://trello.com/invite/b/0xTGfdhA/ATTI723b81d85f9412b7a5f41b8c794eadfc665F35AE/self-service-kiosk)

![Trello 01](docs/Trello_01.png)
![Trello 01](docs/Trello_02.png)
![Trello 01](docs/Trello_03.png)


### R8. Design help documentation which includes a set of instructions which accurately describe how to use and install the application.

You must include:
- steps to install the application  

    - Instructions to access Gus' Restaturant Self Service Kiosk:

    - Open a terminal window on your computer.

    - Navigate to the directory where the RUN_SSKiosk.sh script is located.

    - Run the following command to execute the script:

    ```
    ./RUN_SSKiosk.sh
    ```

    This will check if Python is installed and if venv is available. If both are true, it will create a virtual environment, install Python dependencies, run the ordering_kiosk.py script, and deactivate the virtual environment. If either Python or venv is not installed, the script will exit with an error message.

    If you encounter any issues while running the script, please refer to the error messages for guidance. You can also refer to the following resources for help:

    [Official virtualenv documentation](https://virtualenv.pypa.io/en/latest/installation.html)  
    [Python Packaging User Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

- any dependencies required by the application to operate

    The below are specified in the requirements.txt file

    about-time==4.2.1  
    alive-progress==3.1.5  
    grapheme==0.6.0  
    markdown-it-py==3.0.0  
    mdurl==0.1.2  
    Pygments==2.17.2  
    rich==13.7.0  

- any system/hardware requirements

    Python 3.2 and over
    virtualenv package installed

    Hardware:  
    system specifications that should be sufficient for running Python terminal applications:

    Operating System: Windows 10, macOS, or Linux  
    Processor: Intel Core i3 or AMD Ryzen 3  
    Memory: 4 GB RAM  
    Storage: 256 GB SSD  
    Display: 1366 x 768 resolution

    These specifications should be sufficient for running most Python terminal applications. However, if you are working with large datasets or running computationally intensive applications

- how to use any command line arguments made for the
application  

    No command line arguments were implemented in this application

    The user only inputs numbers, codes or keywords displayed in the user interface