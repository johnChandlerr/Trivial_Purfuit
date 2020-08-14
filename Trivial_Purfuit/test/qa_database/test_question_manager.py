import unittest
import definitions
from Trivial_Purfuit.src.qa_database.question_manager import QuestionManager


class TestQuestionManager(unittest.TestCase):

    def testValidQuestionAndAnswer(self):
        QuestionManager(definitions.ROOT_DIR + "/Trivial_Purfuit/csvs/questions-and-answers.csv")

    def testTooManyColumnsQuestionManagerConstructor(self):
        try:
            QuestionManager(definitions.ROOT_DIR + "/Trivial_purfuit/csvs/too-many-columns.csv")
            self.fail("Should have failed earlier")
        except ValueError:
            pass

    def testTooFewColumnsQuestionManagerConstructor(self):
        try:
            QuestionManager(definitions.ROOT_DIR + "/Trivial_purfuit/csvs/too-few-columns.csv")
            self.fail("Should have failed earlier")
        except ValueError:
            pass

    def testTooFewTypesQuestionManagerConstructor(self):
        try:
            QuestionManager(definitions.ROOT_DIR + "/Trivial_purfuit/csvs/too-few-types.csv")
            self.fail("Should have failed earlier")
        except ValueError:
            pass

    def testTooManyTypesQuestionManagerConstructor(self):
        try:
            QuestionManager(definitions.ROOT_DIR + "/Trivial_purfuit/csvs/too-many-types.csv")
            self.fail("Should have failed earlier")
        except ValueError:
            pass

    def testIncorrectHeadersQuestionManagerConstructor(self):
        try:
            QuestionManager(definitions.ROOT_DIR + "/Trivial_purfuit/csvs/incorrect-headers.csv")
            self.fail("Should have failed earlier")
        except KeyError:
            pass

    def testDifferentQuestionTypesQuestionManagerConstructor(self):
        QuestionManager(definitions.ROOT_DIR + "/Trivial_purfuit/csvs/different-question-types.csv")


if __name__ == '__main__':
    unittest.main()
