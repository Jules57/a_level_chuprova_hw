"""
This module is used for parsing CSV files from URLs to create Candidate class objects.
"""
import csv
import functools
import urllib.request


class Candidate:
    """
    Creates Candidate objects either by initializing object, or by parsing csv file from the URL.
    """
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

    @staticmethod
    def read_from_url(func):
        """
        Parses URL, writes values to a new CSV file with headers.
        :param func: function to decorate
        :return: function
        """
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            """
            This function goes to the URL, receives data,
            decode it and process into lists of values.
            Then it writes them into a new CSV file with headers.
            :param args: None
            :param kwargs: None
            :return: decorated function
            """
            url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
            with urllib.request.urlopen(url) as response:
                lines = [line.decode('utf-8') for line in response.readlines()]
                prepared_list = [item.strip().split(',') for item in lines]
                prepared_list = prepared_list[1:]

            fieldnames = ['Full Name', 'Email', 'Tech Stack', 'Main Skill', 'Main Skill Grade']

            with open('parsed_file.csv', 'w', encoding='utf-8') as infile:
                writer = csv.DictWriter(infile, fieldnames=fieldnames)
                writer.writeheader()
                for item in prepared_list:
                    can_dict = dict(zip(fieldnames, item))
                    writer.writerow(can_dict)
            result = func(*args, **kwargs)
            return result

        return wrapper_decorator

    @classmethod
    @read_from_url
    def generate_candidates(cls, path_to_file):
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
    candidates = Candidate.generate_candidates('parsed_file.csv')
    print([x.full_name for x in candidates])
