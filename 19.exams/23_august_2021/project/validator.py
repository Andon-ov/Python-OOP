class Validator:
    @staticmethod
    def raise_error_if_empty_string_or_whitespace(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)