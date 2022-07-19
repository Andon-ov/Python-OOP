class Validator:
    @staticmethod
    def raise_error_when_model_have_les_4_symbols(value, error_msg):
        if len(value) < 4:
            raise ValueError(error_msg)

    @staticmethod
    def speed_limits(value, min_speed, max_speed, error_msg):
        if not min_speed <= value <= max_speed:
            raise ValueError(error_msg)

    @staticmethod
    def contains_only_white_spaces_or_empty_string(value: str, error_msg):
        if value.split() == "":
            raise ValueError(error_msg)
