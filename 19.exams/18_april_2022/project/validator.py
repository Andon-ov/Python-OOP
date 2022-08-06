from project.user import User


class Validator:

    @staticmethod
    def cannot_be_empty_string_or_whitespace(value: str, error_msg: str):
        if len(value) == 0:
            raise ValueError(error_msg)

    @staticmethod
    def model_cant_be_less_than_4_symbols(value: str, error_msg: str):
        if len(value) < 4:
            raise ValueError(error_msg)

    @staticmethod
    def speed_limit_must_be_between_min_speed_limit_and_max_speed_limit(value, min_speed, max_speed, error_msg: str):
        if value < min_speed or value > max_speed:
            raise ValueError(error_msg)

    @staticmethod
    def cannot_be_less_than_zero(value, error_msg: str):
        if value < 0:
            raise ValueError(error_msg)

    @staticmethod
    def player_name_should_be_unique(value, player_set, error_msg: str):
        if value in player_set:
            raise Exception(error_msg)

    @staticmethod
    def cannot_be_under_6_years_old(value, error_msg):
        if value < 6:
            raise ValueError(error_msg)

    @staticmethod
    def year_cannot_be_under_1888(value, error_msg):
        if value < 1888:
            raise ValueError(error_msg)

    @staticmethod
    def owner_must_be_object_of_type_user(value, error_msg):
        if not isinstance(value, User):
            raise ValueError(error_msg)

    @staticmethod
    def age_restriction_cannot_be_under_min_age_restriction(value, min_age_restriction, error_msg):
        if value < min_age_restriction:
            raise ValueError(error_msg)
