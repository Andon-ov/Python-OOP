class Validator:

    @staticmethod
    def rase_error_for_empty_string(value:str, error_msg):
        if value.strip() == '':
            raise ValueError(error_msg)

    @staticmethod
    def rase_error_for_negative_number(value: int, error_msg):
        if value < 0:
            raise ValueError(error_msg)