from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, name: str, email: str) -> User:
    db_user = User(name=name, email=email)  # create a new User instance
    db.add(db_user)  # add the new user to the session
    db.commit()  # commit the transaction to save the user to the database
    db.refresh(db_user)  # refresh the instance to get the updated data from the database (like id)
    return db_user  # return the newly created user instance

#get all users from the database
def get_users(db: Session):
    return db.query(User).all()  # query the User table and return all user records

#get a user by id
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()  # query the User table for a user with the specified id and return the first match

#update a user's name and email by id
def update_user(db: Session, user_id: int, name: str, email: str):
    user = get_user(db, user_id)  # query the User table for a user with the specified id
    if user:  # if the user exists, update their name and email
        user.name = name
        user.email = email
        db.commit()  # commit the transaction to save the changes to the database
        db.refresh(user)  # refresh the instance to get the updated data from the database
    return user  # return the updated user instance

#delete a user by id
def delete_user(db: Session, user_id: int): 
    user = get_user(db, user_id)  # query the User table for a user with the specified id
    if user:  # if the user exists, delete them from the database
        db.delete(user)  # delete the user from the session
        db.commit()  # commit the transaction to save the changes to the database
    return user  # return the deleted user instance (or None if not found)




