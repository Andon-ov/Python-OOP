class Validator:

    @staticmethod
    def cannot_be_empty_string_or_whitespace(value: str, error_msg: str):
        if value.strip() == '':
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
    def player_cannot_be_under_12_years_old(value, error_msg):
        if value < 12:
            raise ValueError(error_msg)

    @staticmethod
    def stamina_must_by_between_0_and_100(value, error_msg: str):
        if value < 0 or value > 100:
            raise ValueError(error_msg)
