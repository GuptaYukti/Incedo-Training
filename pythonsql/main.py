from database import SessionLocal, engine, Base
from crud import create_user, get_users, get_user, update_user, delete_user

def init_db():
    # create the database tables
    Base.metadata.create_all(bind=engine)

def main(op):
    print("Initializing the database...")
    init_db()
    print("Database initialized successfully!")

## PRESS 1-6 TO PERFORM CRUD OPERATIONS
## 1: Create a new user
## 2: Get all users
## 3: Get a user by ID
## 4: Update a user by ID
## 5: Delete a user by ID   
## 6: Exit
    while op != 6:
        if op == 1: 
            # creating a new user with name and email as user input
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            user = create_user(SessionLocal(), name=name, email=email)
            print("Created user:", user)
            
            # want to add more users? (y/n)
            more = input("Do you want to add more users? (y/n): ")  
            if more.lower() == 'y':
                continue  # continue the loop to add more users
            else:
                print("Exiting user creation.")
                #exit this operation and ask for next operation
                op = int(input("Enter an option (1-6): "))
            
        elif op == 2:
            # getting all users
            users = get_users(SessionLocal())
            print("All users:", users)
            # return to main menu after displaying users
            op = int(input("Enter an option (1-6): "))
            
        elif op == 3:
            # getting a user by ID
            user_id = int(input("Enter user ID to get: "))
            user = get_user(SessionLocal(), user_id)
            print("User with ID", user_id, ":", user)

            # do you want to get another user? (y/n)
            more = input("Do you want to get another user? (y/n): ")    
            if more.lower() == 'y':
                continue  # continue the loop to get another user   
            else:
                print("Exiting user retrieval.")
                # exit this operation and ask for next operation
                op = int(input("Enter an option (1-6): "))

        elif op == 4:
            # updating a user by ID
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            user = update_user(SessionLocal(), user_id, name, email)
            print("Updated user with ID", user_id, ":", user)

            # do you want to update another user? (y/n)
            more = input("Do you want to update another user? (y/n): ")    
            if more.lower() == 'y':
                continue  # continue the loop to get another user   
            else:
                print("Exiting user update.")
                # exit this operation and ask for next operation
                op = int(input("Enter an option (1-6): "))

        elif op == 5:
            # deleting a user by ID
            user_id = int(input("Enter user ID to delete: "))
            user = delete_user(SessionLocal(), user_id)
            print("Deleted user with ID", user_id, ":", user)

            # do you want to delete another user? (y/n)
            more = input("Do you want to delete another user? (y/n): ") 
            if more.lower() == 'y':
                continue  # continue the loop to delete another user   
            else:
                print("Exiting user deletion.")
                # exit this operation and ask for next operation
                op = int(input("Enter an option (1-6): "))
        
        else:
            print("Invalid option. Please enter a number between 1 and 6.")
            op = int(input("Enter an option (1-6): "))


if __name__ == "__main__":
    op= int(input("Enter an option (1-6): "))
    main(op)
