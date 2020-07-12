import definitions
from Trivial_Purfuit.src.die.die import Die
from Trivial_Purfuit.src.qa_database.question_manager import QuestionManager


def die_driver():
    print("\tDie")
    die = Die()
    num = die.roll()
    print("Roll the Die -> return: {}".format(num))


def qa_database():
    print("\n\tQuestion_manger")
    question_manager = QuestionManager(definitions.ROOT_DIR + "/Trivial_Purfuit/csvs/driver.csv")
    # Get correct data type
    print("=> Draw with Correct question type")
    question_type = "Location"
    question = question_manager.get_question(question_type)
    print("Get Database question with <{}> type-> return: {}".format(question_type, question))
    question_type = "People"
    question = question_manager.get_question(question_type)
    print("Get Database question with <{}> type-> return: {}".format(question_type, question))
    question_type = "Event"
    question = question_manager.get_question(question_type)
    print("Get Database question with <{}> type-> return: {}".format(question_type, question))
    question_type = "Independence Day"
    question = question_manager.get_question(question_type)
    print("Get Database question with <{}> type-> return: {}".format(question_type, question))

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


def player_token():
    print("\n\tPlayer_Token")
    print("\n=>Collect cake pieces")
    print("\n=>Player current turn")
    print("\n=>Player current location")


def board():
    print("\n\tBoard")
    print("\n=>Roll again")
    print("\n=>Tiles")
    print("\n=>Assign player round")


die_driver()
qa_database()
player_token()
board()
