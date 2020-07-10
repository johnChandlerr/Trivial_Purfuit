import unittest
import definitions
from Trivial_Purfuit.src.qa_database.question_manager import QuestionManager


class TestQuestionManager(unittest.TestCase):

    def testValidQuestionAndAnswer(self):
        question_manager = QuestionManager(definitions.ROOT_DIR + "/Trivial_Purfuit/csvs/test1.csv")
        question = question_manager.get_question("date")
        self.assertEqual(True, question_manager.check_answer(question, "answer 3"))


if __name__ == '__main__':
    unittest.main()
