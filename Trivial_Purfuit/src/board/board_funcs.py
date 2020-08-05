import definitions
#Assuming this is how the import will go once die class is added

from PySide2.QtWidgets import (QInputDialog, QMessageBox)
from Trivial_Purfuit.src.die import die
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
        #Basic constructor, temporary place holder to ensure these functions compile with no errors
        #And to allow for the skeletal increment demonstration
        #The next increment will have the_board and board_funcs integrated together
        self.qa_manager = QuestionManager(definitions.ROOT_DIR + "/Trivial_Purfuit/csvs/test1.csv")
        self.num_row_tiles = 9
        self.num_col_tiles = 9
        #Assuming 1 die object is managed by the board (at least for now)
        #Rather than individual die objects for each player
        self.die = die.Die()

    def set_round_order(self, players):
        """
        Determines the order in which players will take their turns during the game
        Input: list of player_token objects that are playing the game
        Output: list of player_tokens objects that are sorted based on highest dice roll
        """
        # TODO: Update based on how we eventually store players in the game
        if len(players) == 1:
            return players
        else:
            first_rolls = {}
            for player in players:
                first_rolls[player] = self.die.roll()
            print(first_rolls)
            # TODO: Resolve case where players roll the same number
            dict_sort = sorted(first_rolls.items(), key=lambda x: x[1], reverse=True)
            sorted_players = [x[0] for x in dict_sort]

            return sorted_players

    def ask_question(self, player, tile_type, isCake):
        """
        Interfaces with board, player, and QA manager to get question,
        get player input, verify input, and update accordingly
        Input: Player token who is answering question, the question type, and tile type to determine cake or not
        Output: True/False to determine subsequent action if answer is right
        Using just stdin/stdout for now to show functionality
        """
        question = self.qa_manager.get_question(tile_type)
        answer, valid_input = QInputDialog.getText(self, tile_type + ' Question', question)

        if valid_input:
            correct, answer_string = self.qa_manager.check_answer(question, answer)
            if correct:
                QMessageBox.information(self, 'Message - pythonspot.com', 'Correct!', QMessageBox.Ok, QMessageBox.Ok)
                print("Correct")
                if isCake:
                    player.award_cake_piece(tile_type)
                return True
            else:
                QMessageBox.information(self, 'Message - pythonspot.com', 'Inorrect! correct answer was: ' + answer,
                                        QMessageBox.Ok, QMessageBox.Ok)
                print("Wrong")
                return False
        else:
            print("-----------------------")
            print("--- Input cancelled ---")
            print("-----------------------")

    def tileLand(self, player):
        """
        Determines what to do after the player token moves and has landed on a tile
        Input: The player token who just landed on a tile
        Output: None
        """
        row = player.location[0]
        col = player.location[1]

        tile_type = self.get_tile_type(row, col)

        if tile_type == "roll_again":
            self.move(player)
        elif tile_type == "hub":
            # Print statement to show functionality
            print("You landed on the hub! WIP")
            return
            # TODO: add hub square functionality
        else:
            if self.is_cake_tile(row, col):
                if self.ask_question(player, tile_type, True):
                    self.move(player)
            else:
                if self.ask_question(player, tile_type, False):
                    self.move(player)

    def move(self, player):
        """
        Determines possible moves for the player token based on current location and dice roll
        Input: The player token who is currently moving
        Output: None
        Potential to store known possible moves at each tile based on dice roll
        so that possible moves don't need to be recalculated
        """
        player_row = player.location[0]
        player_col = player.location[1]
        roll = self.die.roll()
        print("Visual purpose roll was: " + str(roll))
        possible_moves = list()

        # TODO: Finish case where player rolls a 6 and goes to nearest cake piece square
        # TODO: Resolve cases where math doesn't check out
        if (roll == 6):
            # Print statement to show functionality
            print("Traveling to the nearest cake piece square! WIP")
        else:
            for row in range(self.num_row_tiles):
                for col in range(self.num_col_tiles):
                    if self.get_tile_type(row, col) != "Invalid":
                        row_diff = row - player_row
                        col_diff = col - player_col
                        total_diff = abs(row_diff) + abs(col_diff)
                        if total_diff == roll:
                            possible_moves.append((row, col))

        # Assumes we add a functionality to the player token class to allow the player to choose where to go
        # Assumes that that functionality will return a 2 element array for row/col coords to update location
        # To be implemented in later increment
        # player.location = player.choose_location(possible_moves)
        # Print statement to show functionality
        for move in possible_moves:
            print("WIP, Possible moves: " + str(move))

        self.tileLand(player)

        """
        Below is a potential WIP implementation of move that would involve iteratively updating
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
    #These functions have been copied from the the_board purely for testing purposes
    #This temporary setup is only needed in order to show off the gui framework in this skeletal increment
    def is_roll_again_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is a holiday tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 0) or (row == 0 and col == 8) or
            (row == 8 and col == 0) or (row == 8 and col == 8)):
            return True
        # end if
    # end isRollAgainTile()

    def is_person_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is a person tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 3) or (row == 0 and col == 6) or
            (row == 1 and col == 0) or (row == 3 and col == 4) or
            (row == 4 and col == 2) or (row == 4 and col == 8) or
            (row == 5 and col == 0) or (row == 7 and col == 4) or
            (row == 8 and col == 1) or (row == 8 and col == 7)):
            return True
        # end if
    # end isPersonTile()

    def is_event_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is an event tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 2) or (row == 0 and col == 5) or
            (row == 2 and col == 0) or (row == 2 and col == 4) or
            (row == 3 and col == 8) or
            (row == 4 and col == 1) or (row == 4 and col == 5) or
            (row == 7 and col == 0) or (row == 7 and col == 8) or
            (row == 8 and col == 4)):
            return True
        # end if
    # end isEventTile()

    def is_place_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is a location/place tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 4) or (row == 1 and col == 8) or
            (row == 3 and col == 0) or
            (row == 4 and col == 3) or (row == 4 and col == 7) or
            (row == 6 and col == 0) or (row == 6 and col == 4) or
            (row == 6 and col == 8) or
            (row == 8 and col == 2) or (row == 8 and col == 5)):
            return True
        # end if
    # end isPlaceTile()

    def is_holiday_tile(self, row, col):
        """
         Description
        -------------
         Checks if the current row and column position is a holiday tile.

         Parameters
        -------------
         (1) row: The selected row on the board.
         (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 1) or (row == 0 and col == 7) or
            (row == 1 and col == 4) or (row == 2 and col == 8) or
            (row == 4 and col == 0) or (row == 4 and col == 6) or
            (row == 5 and col == 4) or (row == 5 and col == 8) or
            (row == 8 and col == 3) or (row == 8 and col == 6)):
            return True
        # end if
    # end isHolidayTile()

    def is_hub_tile(self, row, col):
        """
        Description
        -------------
        Checks if the current row and column position is the hub tile.

        Parameters
        -------------
        (1) row: The selected row on the board.
        (2) col: The selected column on the board.
        """
        if (row == 4 and col == 4):
            return True

    def is_cake_tile(self, row, col):
        """
        Description
        -------------
        Checks if the current row and column position is a cake tile.

        Parameters
        -------------
        (1) row: The selected row on the board.
        (2) col: The selected column on the board.
        """
        if ((row == 0 and col == 4) or (row == 4 and col == 0) or
            (row == 4 and col == 8) or (row == 8 and col ==4)):
            return True

    def get_tile_type(self, row, col):
        """
        Description
        -------------
        Utilizes previous methods for tile checking to return a string of
        what tile type the current row and column position is

        Parameters
        -------------
        (1) row: The selected row on the board.
        (2) col: The selected column on the board.
        """
        if self.is_hub_tile(row, col):
             return "hub"
        elif self.is_person_tile(row, col):
            return "people"
        elif self.is_holiday_tile(row, col):
            return "holiday"
        elif self.is_place_tile(row, col):
            return "place"
        elif self.is_event_tile(row, col):
            return "event"
        elif self.is_roll_again_tile(row, col):
            return "roll_again"
        else:
            return "Invalid"
