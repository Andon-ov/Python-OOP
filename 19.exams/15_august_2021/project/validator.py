class Validator:

    @staticmethod
    def raise_error_if_empty_string_or_whitespace(string:str,message:str):
        if string == '' or string == ' ':
            raise ValueError(message)


    @staticmethod
    def raise_error_if_price_less_than_or_equal_to_zero(value,message:str):
        if value <= 0:
            raise ValueError(message)
