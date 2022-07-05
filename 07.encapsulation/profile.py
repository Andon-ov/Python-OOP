class Profile:
    pass
# username: str - the username should be between 5 and 15 characters (inclusive). If it is not, raise a ValueError with message "The username must be between 5 and 15 characters."
# password: str - the password must be at least 8 characters long; it must contain at least one upper case letter and at least one digit. If it does not, raise a ValueError with message "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
# Hint: Use Getters and Setters to name mangle them.
# Override the __str__() method of the base class so it returns: "You have a profile with username: "{username}" and password: {"*" with the length of password}".






























# class Profile:
#     min_username_len = 5
#     max_username_len = 15
#
#     min_password_len = 8
#     min_uppercase_letters_count = 1
#     min_digits_count = 1
#
#     def __init__(self, username: str, password: str, ):
#         self.username = username
#         self.password = password
#
#     def __validate_username(self, username):
#         if len(username) < self.min_username_len or self.max_username_len < len(username):
#             raise ValueError("The username must be between 5 and 15 characters.")
#
#     def __validate_password(self, password):
#
#         if len(password) < self.min_password_len:
#             raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#         if len([x for x in password if x.isupper()]) < self.min_uppercase_letters_count:
#             raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#         if len([x for x in password if x.isdigit()]) < self.min_digits_count:
#             raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, value):
#         self.__validate_username(value)
#         self.__username = value
#
#     @property
#     def password(self):
#         return ''.join("*" * len(self.__password))
#
#     @password.setter
#     def password(self, value):
#         self.__validate_password(value)
#         self.__password = value
#
#     def __str__(self):
#         return f'You have a profile with username: "{self.username}" and password: {self.password}'
#
#
