from project.library import Library
from project.user import User


class Registration:
    def __init__(self):
        pass

    @staticmethod
    def add_user(user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    # Adds the user if we do not have them in the library's user records already
    # Otherwise, returns the message "User with id = {user_id} already registered in the library!"
    @staticmethod
    def remove_user(user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    # Removes the user from the library records if present
    # Otherwise, returns the message "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id != user_id:
                return f"There is no user with id = {user_id}!"
            if user.user_id == user_id and user.username == new_username:
                return "Please check again the provided username " \
                       "- it should be different than the username used so far!"
            user.username = new_username
            return f"Username successfully changed to: {new_username} for user id: {user_id}"  # userid
        # /Changes his username in the rented_books dictionary as well (if present).

    # If the new username is the same for this id, returns the following message
    # /"Please check again the provided username - it should be different than the username used so far!".

    # If there is no record for the provided id returns
    # /"There is no user with id = {user_id}!"

    # If there is a record with the same user id in the library and the username is different than the provided one,
    # /changes the username with the new one provided and returns the message
    # /"Username successfully changed to: {new_username} for user id: {user_id}".
    # /Changes his username in the rented_books dictionary as well (if present).
