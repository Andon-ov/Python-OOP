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
    def raise_error_if_value_not_between_min_and_max(value, min_value, max_value message: str):
        if value > max_value or value < min_value:
            raise ValueError(message)
