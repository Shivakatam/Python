user_database = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username exists and passwords match
    if username in user_database and user_database[username] == password:
        print("Login successful")
    else:
        print("Login failed. Please check your username and password.")

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    if username in user_database:
        print("Username already exists. Please choose a different username.")
        return
    
    password = input("Enter a password: ")
    user_database[username] = password
    print("Registration successful!")

# Main program loop
while True:
    print("\nWelcome to the login system")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        login()
    elif choice == '2':
        register()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
