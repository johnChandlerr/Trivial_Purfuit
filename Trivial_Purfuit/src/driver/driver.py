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

    # check user input answer
    print("\n=> Check player answer")
    question_type = "Driver Question"
    question = question_manager.get_question(question_type)
    wrong_answer = "Wrong User Input Answer"
    correct_answer = "driver answer"
    wrong_result = question_manager.check_answer(question, wrong_answer)
    correct_result = question_manager.check_answer(question, correct_answer)
    print("Player answer incorrect -> Result:{}".format(wrong_result))
    print("Player answer correct  -> Result:{}".format(correct_result))


def player_token_driver():
    print("\n\tPlayer Token")
    token = PlayerToken('Player1')
    # check a cake piece has been given
    cake_category = 'people'
    result = token.check_cake_piece(cake_category)
    print("=>Collect cake pieces")
    print("Token:{} includes Cake Type:{} ->Result: {}".format(token.name, cake_category, result))
    print("\n=>Award cake pieces")
    # check award a cake piece
    token.award_cake_piece(cake_category)
    print("Token:{} award Cake Type:{}".format(token.name, cake_category))
    result = token.check_cake_piece(cake_category)
    print("Token:{} includes Cake Type:{} ->Result: {}".format(token.name, cake_category, result))


def board_funcs_driver():
    print("\n\tBoard Function")
    token = PlayerToken('Player1')
    board_function = board_funcs()
    # Ask question and collect cake
    print("\n=>Ask question")
    q_type = 'date'
    title_type = 'cake'
    board_function.ask_question(token, q_type, title_type)
    print("\n=>Player Tile Land")
    # board_function.tileLand(token)
    print("\n=>Player round order")
    # board_function.set_round_order()
    print("\n=>Player move")
    board_function.move()


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
# player_token_driver()
# board()
