






























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
