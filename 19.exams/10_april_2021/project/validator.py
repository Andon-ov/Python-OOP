class Validator:

    @staticmethod
    def cannot_be_empty_string(value, error_msg):
        if value == "":
            raise ValueError(error_msg)

    @staticmethod
    def cannot_be_equal_to_or_below_zero(value, error_msg):
        if value <= 0:
            raise ValueError(error_msg)
