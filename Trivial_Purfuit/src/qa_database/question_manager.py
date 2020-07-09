import pandas
import random


class QuestionManager:
    """
    The interface to interact with the Question/Answer Database
    """
    def __init__(self, csv_file_name):
        """
        Construct a QuestionManager instance
        :param csv_file_name: The name of the question/answer database file
        """
        question_answer_df = pandas.read_csv(csv_file_name, header='infer')
        self.type_question_dict = {k: list(v) for k, v in question_answer_df.groupby("type")["question"]}
        self.question_answer_dict = pandas.Series(question_answer_df.answer.values,
                                                  index=question_answer_df.question).to_dict()

    def get_question(self, question_type):
        """
        Get a random question of the provided type
        :param question_type: The type of question the user wants to retrieve
        :return: A random question for the provided type
        """
        return self.type_question_dict[question_type][random.randint(0, len(self.type_question_dict[question_type]) - 1)]

    def check_answer(self, question, answer):
        """
        Check if the provided answer is correct for the provided question
        :param question: The question being answered by the user
        :param answer: The answer provided by the user
        :return: True if correct, False otherwise
        """
        return answer == self.question_answer_dict[question]
