import definitions
from Trivial_Purfuit.src.qa_database.question_manager import QuestionManager

class board_funcs:
    """
    Some basic board functions that we can modify/move/redo as needed
    Anticipating that these are just copied over into the main board class
    once the board data structure/coordinate system is in place
    Assumptions that if wrong the code can easily be changed to accommodate:
    The player_token class responsible for dice rolls
    The coordinate system starts at the bottom left of the board (ie bottom left tile is (0,0))
    The color and tile type (ie cake, hub, roll again, basic/none) are tracked for each tile
    """
    #TODO: Update accordingly once we know how tiles and coordinates are being tracked/stored

    def __init__(self):
        #Basic constructor, really just a place holder to ensure these functions compile with no errors
        self.qa_manager = QuestionManager(definitions.ROOT_DIR + "/Trivial_Purfuit/csvs/test1.csv")
        self.board_tiles = None

    def set_round_order(self, players):
        """
        Determines the order in which players will take their turns during the game
        Input: list of player_token objects that are playing the game
        Output: list of player_tokens objects that are sorted based on highest dice roll
        """
        #TODO: Determine how we track players, if its just an attribute in the board object this doesn't need input,
        #TODO: we can just update the attribute itself stored in the board object
        if len(players) == 1:
            return players
        else:
            first_rolls = {}
            for player in players:
                first_rolls[player] = player.get_dice_roll()

            #TODO: Resolve case where players roll the same number
            dict_sort = sorted(first_rolls.items(), key=lambda x: x[1], reverse=True)
            sorted_players = [x[0] for x in dict_sort]

            return sorted_players

    def ask_question(self, player, q_type, tile_type):
        """
        Interfaces with board, player, and QA manager to get question,
        get player input, verify input, and update accordingly
        Input: Player token who is answering question, the question type, and tile type to determine cake or not
        Output: True/False to determine subsequent action if answer is right
        Using just stdin/stdout for now
        """
        question = self.qa_manager.get_question(q_type)
        print(question)
        answer = input("Type your answer: ")
        if self.qa_manager.check_answer(question, answer):
            print("Correct")
            if tile_type == "cake":
                player.award_cake_piece(q_type)
            return True
        else:
            print("Wrong")
            return False

    def tileLand(self, player):
        """
        Determines what to do after the player token moves and has landed on a tile
        Input: The player token who just landed on a tile
        Output: None
        """
        coord = player.location
        tile_type = self.get_tile_type(coord)

        if tile_type == "roll_again":
            self.move(player)
        elif tile_type == "hub":
            return
            #TODO: add hub square functionality
        else:
            q_type = self.get_tile_color(coord)
            if self.ask_question(player, q_type, tile_type):
                self.move(player)

    def move(self, player):
        """
        Determines possible moves for the player token based on current location and dice roll
        Input: The player token who is currently moving
        Output: None
        Potential to store known possible moves at each tile based on dice roll
        so that possible moves don't need to be recalculated
        """
        coord = player.location
        roll = player.get_dice_roll()
        possible_moves = list()

        #TODO: Resolve case where player rolls 6 and is located in certain tiles where this
        #TODO: doesn't return all of the correct possible locations
        for tile in self.board_tiles:
            x_diff = tile.x - coord.x
            y_diff = tile.y - coord.y
            total_diff = abs(x_diff) + abs(y_diff)
            if total_diff == roll:
                possible_moves.append(tile)

        #Assumes we add a functionality to the player token class to allow the player to choose where to go
        #Assumes that that functionality will return a coord and can just be used to update the player token location
        player.location = player.choose_location(possible_moves)
        self.tileLand(player)

        """
        Below is a potential implementation of move that would involve iteratively updating
        player location as they move. Not completed, would need methods that can retrieve valid directions
        and would allow player to choose a direction from a list of directions 

        #Assume get_dir returns a list of available directions to move
        valid_dir = self.get_dir(coord)
        chosen_dir = player.choose_dir(valid_dir)
        while roll > 0:
            #Update player location based on direction moved
            valid_dir = self.get_dir(player.location)
            #If # valid directions is 2 then we're just in a straight line on the board
            if len(valid_dir) > 2:
                #Remove the previously chosen direction to make sure player can't just go backwards
                new_dir = valid_dir.remove(chosen_dir)
                chosen_dir = player.choose_dir(new_dir)

            roll -= 1
         self.tileLand(player)
        """
