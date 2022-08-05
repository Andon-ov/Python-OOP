class Validator:
    @staticmethod
    def cannot_be_empty_string_or_whitespace(value: str, error_msg: str):
        if value.strip() == '':
            raise ValueError(error_msg)
