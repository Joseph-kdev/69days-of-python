import random

names = ['Alex', 'Caroline', 'John', 'Eleanor', 'Catherine']

student_scores = {name:random.randint(1, 100) for name in names}

passed_students = {key:value for key,value in student_scores.items() if value > 40}

print(passed_students)