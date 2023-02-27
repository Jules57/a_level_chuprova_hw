"""
This module is used to create csv files with headers and records.
"""
import csv


def create_csv(filename: str):
    """
    Creates a new csv file with headers.
    :param filename: string, path to file
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as csv_file:
        fieldnames = ['Full Name', 'Email', 'Tech Stack', 'Main Skill', 'Main Skill Grade']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()


def record_csv(filename: str):
    """
    Records dicts into the csv file provided.
    :param filename: string, path to file
    :return: None
    """
    create_csv(filename)
    with open(filename, 'a', encoding='utf-8') as csv_file:
        fieldnames = ['Full Name', 'Email', 'Tech Stack', 'Main Skill', 'Main Skill Grade']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerows([
            {
                'Full Name': 'Ivan Checkov',
                'Email': 'ichech@example.com',
                'Tech Stack': ['Python', 'Django', 'Angular'],
                'Main Skill': 'Python',
                'Main Skill Grade': 'Senior'},
            {
                'Full Name': 'Max Payne',
                'Email': 'mpayne@example.com',
                'Tech Stack': ['PHP', 'Laravel', 'MysQL'],
                'Main Skill': 'PHP',
                'Main Skill Grade': 'Middle'},
            {
                'Full Name': 'Tom Hanks',
                'Email': 'thanks@example.com',
                'Tech Stack': ['Python', 'CSS'],
                'Main Skill': 'Python',
                'Main Skill Grade': 'Junior'},
            {
                'Full Name': 'David Bowie',
                'Email': 'dbowie@example.com',
                'Tech Stack': ['Python', 'Django', 'Flask', 'Docker', 'PostgreSQL'],
                'Main Skill': 'Python',
                'Main Skill Grade': 'Senior+'
            }])
