"""
This module is used for parsing CSV files to create Candidate class objects.
"""

import csv

import create_candidates


class Candidate:
    """Creates Candidate objects either by initializing object, or by parsing csv file."""
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        """
        Initialization
        :param first_name: string
        :param last_name: string
        :param email: string
        :param tech_stack: list of strings
        :param main_skill: string, the best skill from tech_stack
        :param main_skill_grade: string ('Senior', 'Middle' or 'Junior')
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        """
        Creates a full name from two attributes: first_name and last_name.
        :return: full name separated with space
        """
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, path_to_file: str):
        """
        Processes CSV file and provides values to initialize Candidate class objects.
        :param path_to_file: filename
        :return: list of Candidate objects
        """
        with open(path_to_file, 'r', encoding='utf-8') as outfile:
            reader = csv.DictReader(outfile)
            candidate_data_prepared = []
            for record in reader:
                candidate = dict(
                        first_name=record['Full Name'].split(' ', maxsplit=1)[0],
                        last_name=record['Full Name'].split(' ', maxsplit=1)[1],
                        email=record['Email'],
                        tech_stack=record['Tech Stack'],
                        main_skill=record['Main Skill'],
                        main_skill_grade=record['Main Skill Grade']
                )
                candidate_data_prepared.append(candidate)
        return [cls(**x) for x in candidate_data_prepared]


if __name__ == '__main__':
    create_candidates.record_csv('candidates_data.csv')
    candidates = Candidate.generate_candidates('candidates_data.csv')
    print([x.full_name for x in candidates])
