class Validator:

    @staticmethod
    def raise_error_if_empty_string_or_whitespace(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_error_if_price_less_than_or_equal_to_zero(value, message: str):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_error_if_value_less_18(value, message: str):
        if value < 18:
            raise ValueError(message)

    #     less than 4 symbols
    @staticmethod
    def raise_error_if_be_a_less_than_4_symbols(value, message: str):
        if len(value) < 4:
            raise ValueError(message)

    @staticmethod
    def raise_error_if_be_more_den_max_horse_speed(value, max_hores_speed, message: str):
        if value > max_hores_speed:
            raise ValueError(message)

    @staticmethod
    def raise_error_when_have_invalid_race_type(value, message: str):
        valid_race_type = {"Winter", "Spring", "Autumn", "Summer"}
        if value not in valid_race_type:
            raise ValueError(message)
