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
    def raise_error_if_value_not_between_1_and_50(value, message: str):
        if value > 50 or value < 1:
            raise ValueError(message)

    @staticmethod
    def raise_error_if_value_not_between_51_and_100(value, message: str):
        if value > 100 or value < 51:
            raise ValueError(message)

