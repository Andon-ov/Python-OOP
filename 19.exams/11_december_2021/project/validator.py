class Validator:
    @staticmethod
    def raise_error_when_model_have_les_4_symbols(value, error_msg):
        if len(value) < 4:
            raise ValueError(error_msg)
