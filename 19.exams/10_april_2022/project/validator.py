from project.controller import Controller


class Validator:

    @staticmethod
    def raise_error_for_empty_string(value: str, error_msg):
        if value.strip() == '':
            raise ValueError(error_msg)

    @staticmethod
    def raise_error_for_negative_number(value: int, error_msg):
        if value < 0:
            raise ValueError(error_msg)

    @staticmethod
    def raise_error_two_players_with_the_same_name(value: int, error_msg):
        if value in Controller.all_players_names:
            raise Exception(error_msg)

    @staticmethod
    def raise_error_if_player_les_12(value: int, error_msg):
        if value < 12:
            raise ValueError(error_msg)

    @staticmethod
    def raise_error_if_stamina_more_den_100_or_les_den_0(value: int, error_msg):
        if value > 100 or value < 0:
            raise ValueError(error_msg)
