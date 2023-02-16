students = {
    'Johnny Walker': ['Python', 'JavaScript'],
    'Jim Beam': ['FrontEnd'],
    'Jack Daniels': ['Java'],
    'Hankey Bannister': ['Fullstack'],
    'Mountain Dew': ['Python', 'FrontEnd', 'Java']
    }

active_students = [key for key, val in students.items() if len(val) > 1]

not_frontend_students = [key for key, val in students.items() if 'FrontEnd' not in val]

python_java_students = [key for key, val in students.items() if 'Python' in val or 'Java' in val]

print(f'Active students: {", ".join(active_students)}.')
print(f'Students that do not learn FrontEnd: {", ".join(not_frontend_students)}.')
print(f'Python or Java students: {", ".join(python_java_students)}.')
