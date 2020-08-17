import pandas
import random
import math

import definitions
from Trivial_Purfuit.src.utils.circular_queue import CircularQueue


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

        # Ensure the CSV file has only 3 columns
        if len(question_answer_df.columns) != 3:
            raise ValueError("the file: " + csv_file_name + " has too many columns...should have (3)")

        for index, row in question_answer_df.head().iterrows():
            for element in row:
                if type(element) != str and math.isnan(element):
                    raise ValueError("the file: " + csv_file_name + " does not have enough columns...should have (3)")

        type_question_dict = {k: list(v) for k, v in question_answer_df.groupby("type")["question"]}

        # Ensure the CSV file has only 4 different question types
        if len(type_question_dict) != 4:
            raise ValueError("the file: " + csv_file_name + " does not have the correct number of types (4)")

        self.type_question_dict_queue = dict()

        for question_type in type_question_dict:
            self.type_question_dict_queue[question_type] = CircularQueue(type_question_dict[question_type])

        # Set the question type variables in definitions.py
        question_types = list(self.type_question_dict_queue.keys())
        definitions.question_type1 = question_types[0]
        definitions.question_type2 = question_types[1]
        definitions.question_type3 = question_types[2]
        definitions.question_type4 = question_types[3]

        self.question_answer_dict = pandas.Series(question_answer_df.answer.values,
                                                  index=question_answer_df.question).to_dict()

    def get_question(self, question_type):
        """
        Get a random question of the provided type
        :param question_type: The type of question the user wants to retrieve
        :return: A random question for the provided type
        """
        return self.type_question_dict_queue[question_type].dequeue()

    def check_answer(self, question, answer):
        """
        Check if the provided answer is correct for the provided question
        :param question: The question being answered by the user
        :param answer: The answer provided by the user
        :return: (True, <answer_string>) if correct, (False, <answer_string>) otherwise
        """
        return answer == self.question_answer_dict[question], self.question_answer_dict[question]
