import definitions

from PySide2.QtWidgets import (QInputDialog, QMessageBox)


class board_funcs:

    def set_round_order(self, players):
        """
        Determines the order in which players will take their turns during the game
        Input: list of player_token objects that are playing the game
        Output: list of player_tokens objects that are sorted based on highest dice roll
        """
        if len(players) == 1:
            return players
        else:
            first_rolls = {}
            for player in players:
                QMessageBox.information(self, 'Who Goes First?', player.name + ' roll the die!', QMessageBox.Ok, QMessageBox.Ok)
                first_rolls[player] = self.die.roll()

            #Covers the case where players rolled the same number on their initial roll
            #Only allows 1 roll off. If the players roll the same number again, turn order is sorted by name
            second_rolls = {}
            for player in players:
                temp_dict = first_rolls.copy()
                temp_dict.pop(player)
                if first_rolls[player] in temp_dict.values():
                    QMessageBox.information(self, 'Who Goes First?', "Roll Off!\n" + player.name + ' reroll the die!',
                                            QMessageBox.Ok, QMessageBox.Ok)
                    second_rolls[player] = self.die.roll()
                else:
                    second_rolls[player] = 0

            for player in players:
                first_rolls[player] = first_rolls[player] + (0.1 * second_rolls[player])

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
                QMessageBox.information(self, 'Your answer was...', 'Correct!', QMessageBox.Ok, QMessageBox.Ok)
                print("Correct")
                if isCake:
                    player.award_cake_piece(tile_type)
                return True
            else:
                QMessageBox.information(self, 'Your answer was...', 'Incorrect! Correct answer was: ' + answer_string,
                                        QMessageBox.Ok, QMessageBox.Ok)
                print("Wrong")
                return False
        else:
            print("-----------------------")
            print("--- Input cancelled ---")
            print("-----------------------")
