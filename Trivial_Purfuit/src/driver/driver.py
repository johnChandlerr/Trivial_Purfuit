import definitions
import sys

from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtWidgets import (QPushButton, QTextEdit)
from PySide2.QtGui import (QPainter, QPen, QBrush)
from PySide2.QtCore import (Qt, SIGNAL)
from Trivial_Purfuit.src.board.board_funcs import board_funcs
from Trivial_Purfuit.src.die.die import Die
from Trivial_Purfuit.src.player_token.player_token import PlayerToken
from Trivial_Purfuit.src.qa_database.question_manager import QuestionManager


def die_driver():
    print("--------------")
    print("\tRoll the Die")
    die = Die()
    num = die.roll()
    print("Die number: {}".format(num))


# get question and check answer
def get_question(question_manager, question_type):
    question = question_manager.get_question(question_type)
    print("Question type: <{}>".format(question_type))
    print("Question: {}".format(question))
    user_ans = input("Answer: ")
    result = question_manager.check_answer(question, user_ans)
    if result:
        print("Correct")
    else:
        print("Wrong")


def qa_database_driver():
    print("\n\tQuestion_manger")
    question_manager = QuestionManager(definitions.ROOT_DIR + "/Trivial_Purfuit/csvs/driver.csv")
    # Get correct data type
    running = True
    while running:
        print("--------------")
        print("=> Get Correct question type")
        print("\t1: people")
        print("\t2: event")
        print("\t3: location")
        print("\t4: holiday")
        print("\t0: === Go Back ===")
        user_input = input("Please select: ")
        if user_input == '1':
            get_question(question_manager, 'People')
        elif user_input == '2':
            get_question(question_manager, 'Event')
        elif user_input == '3':
            get_question(question_manager, 'Location')
        elif user_input == '4':
            get_question(question_manager, 'Holiday')
        elif user_input == '0':
            running = False
        else:
            print("\tSorry, \"{}\" is not valid. Please try again.".format(user_input))


def show_token_status(token):
    print("Player token: " + token.name)
    for k, v in token.cake_list.items():
        print("Cake:{} Awarded:{}".format(k, v))


def award_cake_piece(token, cake_category):
    # hard code for awarded cake piece
    token.award_cake_piece(cake_category)


def player_token_driver():
    print("\n\tPlayer Token")
    player_name = input("Player name: ")
    token = PlayerToken(player_name)
    running = True
    while running:
        print("--------------")
        print("=> Player Token")
        print("\t1: Show Token Status")
        print("\t2: Award <people> cake piece")
        print("\t3: Award <event> cake piece")
        print("\t4: Award <place> cake piece")
        print("\t5: Award <holiday> cake piece")
        print("\t0: === Go Back ===")
        user_input = input("Please select: ")
        if user_input == '1':
            show_token_status(token)
        elif user_input == '2':
            award_cake_piece(token, "people")
        elif user_input == '3':
            award_cake_piece(token, "event")
        elif user_input == '4':
            award_cake_piece(token, "place")
        elif user_input == '5':
            award_cake_piece(token, "holiday")
        elif user_input == '0':
            running = False
        else:
            print("\tSorry, \"{}\" is not valid. Please try again.".format(user_input))


def board_funcs_driver():
    print("\n\tBoard Function")
    # token = PlayerToken('Player1')
    # board_function = board_funcs()
    # Ask question and collect cake
    print("\n=>Ask question")
    # q_type = 'date'
    # title_type = 'cake'
    # board_function.ask_question(token, q_type, title_type)
    print("\n=>Player Tile Land")
    # board_function.tileLand(token)
    print("\n=>Player round order")
    # board_function.set_round_order()
    print("\n=>Player move")
    # board_function.move()


def main():
    app = QApplication(sys.argv)
    running = True
    while running:
        print("=================")
        print("Subsystem Menu:")
        print("\t1: Roll die")
        print("\t2: Q/A database")
        print("\t3: Player token")
        print("\t4: Board function")
        print("\t0: === Exit ===")
        user_input = input("Please select: ")
        if user_input == '1':
            die_driver()
        elif user_input == '2':
            qa_database_driver()
        elif user_input == '3':
            player_token_driver()
        elif user_input == '4':
            board_funcs_driver()
        elif user_input == '0':
            running = False
        else:
            print("\tSorry, \"{}\" is not valid. Please try again.".format(user_input))


if __name__ == "__main__":
    main()
