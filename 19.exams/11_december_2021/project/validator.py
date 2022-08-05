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
