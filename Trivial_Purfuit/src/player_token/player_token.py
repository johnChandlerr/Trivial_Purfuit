

class PlayerToken:
    """
    The Player Token class to store game progress per player and interact with Board.
    """
    def __init__(self, player_name):
        """
        Construct a PlayerToken instance for a player based on name Provided by Board and an empty cake piece Dictionary
        """
        self.name = player_name
        self.cake_list = {
            "people":False,
            "event":False,
            "place":False,
            "holiday":False}
        self.turn_status = False
        self.location = []

    def check_cake_piece(self,cake_category):
        """
        Check whether a cake piece has been given for a cake_category, if cake piece not awarded, then award
        :param cake_category:
        :return: indication that cake piece has been awarded
        """
        return self.cake_list[cake_category]


    def award_cake_piece(self, cake_category):
        """
        Get a random question of the provided type
        :param question_type: The type of question the user wants to retrieve
        :return: Confirmation of cake piece type awarded
        """
        if self.cake_list[cake_category] == False:
            self.cake_list[cake_category] = True