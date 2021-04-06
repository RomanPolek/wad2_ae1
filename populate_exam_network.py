#!/bin/python

# Database population script for Exam Network
# Has to be run on a clean database, otherwise it will fail due to User conflicts
# Most student's submissions will have 0 or very low grades, that's expected
# The script randomly generates the answers to questions so lots of them end up being wrong answers


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_ae1.settings')
import django
import django.contrib.auth

from random import seed, randint
seed(1)

django.setup()

from django.contrib.auth.models import User
from exam_network.models import Profile, Course, Question, Exam, Answer, Submission
import datetime

teachers = [
    {"first_name": "Emma",
     "last_name": "Jackson",
     "email": "emma.jackson@test.com",
     "password": "Parking678"},

    {"first_name": "Robert",
     "last_name": "Collins",
     "email": "robert.collins@.com",
     "password":"Blanchard4637"},

    {"first_name": "Kelly",
     "last_name": "Donovan",
     "email": "kelly.donovan@test.com",
     "password": "BestTeacherEver8786"},

    {"first_name":"John",
     "last_name":"Brown",
     "email":"john.brown@test.com",
     "password":"ForestGump315"}
     ]

students = [
    {"first_name":"Owen",
     "last_name":"Nichols",
     "email":"o.nichols.9063@test.com",
     "password":"Aliquam2501"},

    {"first_name":"Brennan",
     "last_name":"Solomon",
     "email":"b.solomon.4258@test.com",
     "password":"Egestasuo2548"},

    {"first_name":"Kieran",
     "last_name":"Parrish",
     "email":"k.parrish.5269@test.com",
     "password":"Bazylleus6958"},

    {"first_name":"Hector",
     "last_name":"Holman",
     "email":"h.holman.5412@test.com",
     "password":"Mauritius58596"},

    {"first_name":"Monica",
     "last_name":"Spencer",
     "email":"m.spencer.4173@test.com",
     "password":"BerriesBlue4587"},

    {"first_name":"Ashley",
     "last_name":"Bradley",
     "email":"a.bradley.5603@test.com",
     "password":"Plecerat2589"},

    {"first_name":"Martha",
     "last_name":"Baldwin",
     "email":"m.baldwin.3021@test.com",
     "password":"Morales33199"},

    {"first_name":"Ashton",
     "last_name":"Mullen",
     "email":"a.mullen.1045@test.com",
     "password":"Volareso5647"},

    {"first_name":"Mark",
     "last_name":"Carney",
     "email":"a.carney.3026@test.com",
     "password":"Nedipinto63021"},

    {"first_name":"Dale",
    "last_name":"Beasley",
    "email":"d.beasley9875@test.com",
    "password":"Faucibus9568"}
    ]

courses = [
    {"name":"History 2",
    "teacher":"emma.jackson@test.com",
    "students": ["o.nichols.9063@test.com", "k.parrish.5269@test.com", "m.spencer.4173@test.com", "m.baldwin.3021@test.com", "a.mullen.1045@test.com"],
    "description":"20th century - events & inventions "},

    {"name":"Anatomy 1",
    "teacher":"robert.collins@.com",
    "students": ["b.solomon.4258@test.com", "k.parrish.5269@test.com", "a.bradley.5603@test.com", "a.carney.3026@test.com"],
    "description":"Advanced course in Human Body"},

    {"name":"Computing Science 1",
    "teacher":"kelly.donovan@test.com",
    "students": ["o.nichols.9063@test.com", "h.holman.5412@test.com", "a.bradley.5603@test.com", "a.carney.3026@test.com"],
    "description":"Advanced course in Algebra"},

    {"name":"English Literature",
    "teacher":"john.brown@test.com",
    "students": ["b.solomon.4258@test.com", "h.holman.5412@test.com", "m.spencer.4173@test.com"],
    "description":"Advanced course in English Literature"},

    {"name":"Geography 2",
    "teacher":"john.brown@test.com",
    "students": ["o.nichols.9063@test.com", "k.parrish.5269@test.com", "a.bradley.5603@test.com"],
    "description":"Advanced course in Geography"}
    ]
exams = [
    {"title":"CS Exam 1",
    "date_available": datetime.datetime(2021,3,20,9,0,0),
    "deadline":datetime.datetime(2021,3,21,0,0,0),
    "course":"Computing Science 1"},

    {"title":"His Exam 1",
    "date_available": datetime.datetime(2021,3,28,13,15,0),
    "deadline":datetime.datetime(2021,3,29,23,30,0),
    "course":"History 2"},

    {"title":"Ana Exam 1",
    "date_available": datetime.datetime(2021,5,18,11,0,0),
    "deadline":datetime.datetime(2021,5,19,0,0,0),
    "course":"Anatomy 1"},

    {"title":"Ana Exam 2",
    "date_available": datetime.datetime(2021,5,12,12,0,0),
    "deadline":datetime.datetime(2021,5,13,0,0,0),
    "course":"Anatomy 1"},

    {"title":"Geo Exam 1",
    "date_available": datetime.datetime(2021,4,6,11,30,0),
    "deadline":datetime.datetime(2021,5,9,0,0,0),
    "course":"Geography 2"}
    ]

questions = [
    {"exam": "CS Exam 1",
    "content":"Which of the following bit patterns represents the value 5?",
    "choice_1":"00010101",
    "choice_2":"00011100",
    "choice_3":"00000101",
    "choice_4":"00001101",
    "choice_5":"00001100",
    "correct_answer":2},

    {"exam": "CS Exam 1",
    "content":"Which of the following bit patterns represents the value 15?",
    "choice_1":"00001111",
    "choice_2":"00001001",
    "choice_3":"00101001",
    "choice_4":"00111001",
    "choice_5":"00011101",
    "correct_answer":0},

    {"exam": "CS Exam 1",
    "content":"Which of the following bit patterns represents the value 10?",
    "choice_1":"00001010",
    "choice_2":"10001010",
    "choice_3":"10101010",
    "choice_4":"00101010",
    "choice_5":"00001000",
    "correct_answer":0},

    {"exam": "CS Exam 1",
    "content":"Which of the following bit patterns represents the value 100?",
    "choice_1":"01100111",
    "choice_2":"01111100",
    "choice_3":"01100111",
    "choice_4":"01111111",
    "choice_5":"01100100",
    "correct_answer":4},

    {"exam": "CS Exam 1",
    "content":"Which of the following bit patterns represents the value 255?",
    "choice_1":"11100011",
    "choice_2":"11111110",
    "choice_3":"11111111",
    "choice_4":"11000110",
    "choice_5":"11010101",
    "correct_answer":2},

    {"exam": "His Exam 1",
    "content":"In which year did World War II start?",
    "choice_1":"1944",
    "choice_2":"1938",
    "choice_3":"1943",
    "choice_4":"1939",
    "choice_5":"1940",
    "correct_answer":3},

    {"exam":"His Exam 1",
    "content":"In which year did World War II end?",
    "choice_1":"1945",
    "choice_2":"1955",
    "choice_3":"1949",
    "choice_4":"1939",
    "choice_5":"1959",
    "correct_answer":0},

    {"exam":"His Exam 1",
    "content":"In which year was London due to host the Olympic Games, but couldn't because of the Second World War?",
    "choice_1":"1950",
    "choice_2":"1955",
    "choice_3":"1930",
    "choice_4":"1939",
    "choice_5":"1944",
    "correct_answer":4},

    {"exam":"His Exam 1",
    "content":"In which year the League of Nations was formed?",
    "choice_1":"1950",
    "choice_2":"1920",
    "choice_3":"1930",
    "choice_4":"1940",
    "choice_5":"1910",
    "correct_answer":1},

    {"exam":"His Exam 1",
    "content":"when did women cast their first vote in America?",
    "choice_1":"1915",
    "choice_2":"1929",
    "choice_3":"1919",
    "choice_4":"1910",
    "choice_5":"1920",
    "correct_answer":4},

    {"exam":"Ana Exam 1",
    "content":"Where is the pharynx located?",
    "choice_1":"neck",
    "choice_2":"head",
    "choice_3":"foot",
    "choice_4":"arm",
    "choice_5":"leg",
    "correct_answer":0},

    {"exam":"Ana Exam 1",
    "content":"Which of these glands produces tears?",
    "choice_1":"lattimmi",
    "choice_2":"lechamal",
    "choice_3":"fareal",
    "choice_4":"laryngeal",
    "choice_5":"lachrymal",
    "correct_answer":4},

    {"exam":"Ana Exam 1",
    "content":"Where is the esophagus located?",
    "choice_1":"chest",
    "choice_2":"head",
    "choice_3":"arm",
    "choice_4":"leg",
    "choice_5":"neck",
    "correct_answer":0},

    {"exam":"Ana Exam 1",
    "content":"What hormone, produced in the pancreas, regulates blood sugar levels?",
    "choice_1":"oxytocin",
    "choice_2":"epinephrine",
    "choice_3":"insulin",
    "choice_4":"prolactin",
    "choice_5":"serotonin",
    "correct_answer":2},

    {"exam":"Ana Exam 1",
    "content":"What is the name of the system in the human body that transports blood?",
    "choice_1":"cardiovascular",
    "choice_2":"lymphatic",
    "choice_3":"respiratory",
    "choice_4":"digestive",
    "choice_5":"endocrine",
    "correct_answer":0},

    {"exam":"Ana Exam 2",
    "content":"Which of these is a neurological disorder?",
    "choice_1":"alopecia",
    "choice_2":"psiatica",
    "choice_3":"Hashimoto syndrome",
    "choice_4":"Alzheimer disease",
    "choice_5":"ticapecia",
    "correct_answer":3},

    {"exam":"Ana Exam 2",
    "content":"Where are red blood corpuscles formed?",
    "choice_1":"bones",
    "choice_2":"heart",
    "choice_3":"lungs",
    "choice_4":"eyes",
    "choice_5":"nose",
    "correct_answer":0},

    {"exam":"Ana Exam 2",
    "content":"Where are red blood corpuscles formed?",
    "choice_1":"bones",
    "choice_2":"heart",
    "choice_3":"lungs",
    "choice_4":"eyes",
    "choice_5":"nose",
    "correct_answer":0},

    {"exam":"Ana Exam 2",
    "content":"What is the formation of new blood vessels called?",
    "choice_1":"Manugenesis",
    "choice_2":"Osteogenesis",
    "choice_3":"Catheterization",
    "choice_4":"Angiogenesis",
    "choice_5":"Angioterization",
    "correct_answer":3},

    {"exam":"Ana Exam 2",
    "content":"What separates the lobes of the lungs from one another?",
    "choice_1":"Tissure",
    "choice_2":"Hilum",
    "choice_3":"Trachea",
    "choice_4":"Pleura",
    "choice_5":"Fissure",
    "correct_answer":3},

    {"exam":"Geo Exam 1" ,
    "content":"What is the capital of Mozambique?",
    "choice_1":"Madrid",
    "choice_2":"Casablanca",
    "choice_3":"Maputo",
    "choice_4":"Kano",
    "choice_5":"Bangui",
    "correct_answer":2},

    {"exam":"Geo Exam 1",
    "content":"Which country is the chief home of the Shona people?",
    "choice_1":"Egypt",
    "choice_2":"Angola",
    "choice_3":"Namibia",
    "choice_4":"Kenya",
    "choice_5":"Zimbabwe",
    "correct_answer":4},

    {"exam":"Geo Exam 1",
    "content":"Serengeti National Park is in which country?",
    "choice_1":"Tanzania",
    "choice_2":"Mali",
    "choice_3":"Niger",
    "choice_4":"Botswana",
    "choice_5":"Sudan",
    "correct_answer":2},

    {"exam":"Geo Exam 1",
    "content":"Which country was formerly called Rhodesia?",
    "choice_1":"Zimbabwe",
    "choice_2":"Algeria",
    "choice_3":"Ghana",
    "choice_4":"Liberia",
    "choice_5":"Guinea",
    "correct_answer":2},

    {"exam":"Geo Exam 1",
    "content":"Which lake is the largest lake in Africa and the main reservoir of the Nile?",
    "choice_1":"Lake Victoria",
    "choice_2":"Lake Tanganyika",
    "choice_3":"Lake Sualiki",
    "choice_4":"Lake Gahauli",
    "choice_5":"Lake Guaru",
    "correct_answer":2}

    ]


def populate():
    for teacher in teachers:
       add_teacher(teacher['first_name'], teacher['last_name'], teacher['email'], teacher['password'])

    for student in students:
       add_student(student['first_name'], student['last_name'], student['email'], student['password'])

    for course in courses:
       add_course(course['name'], course['description'], course['teacher'], students=course['students'])

    for exam in exams:
        exam_questions = [q for q in questions if q['exam'] == exam['title']]
        final_questions = []

        for q in exam_questions:
            question = add_question(q['content'], [q['choice_1'],q['choice_2'],q['choice_3'],q['choice_4'],q['choice_5']], q['correct_answer'])
            final_questions.append(question)

        add_exam(exam['title'], exam['course'], exam['date_available'], exam['deadline'], final_questions)


    # Randomly generate submissions
    for course in Course.objects.all():
        course_students = course.students.all()

        for student in course_students:
            for exam in course.exam_set.all():
                print(student, exam)
                exam_answers = []
                for question in exam.questions.all():
                    ans = add_answer(question, randint(0, 4))
                    exam_answers.append(ans)
                add_submission(exam, student, exam_answers)


def add_teacher(first_name, last_name, email, password):
    user = User.objects.create_user(email, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.profile.role = 'T'
    user.save()
    return user


def add_student(first_name, last_name, email, password):
    user = User.objects.create_user(email, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.profile.role = 'S'
    user.save()
    return user


def add_course(name, description, teacher, students=None):
    course = Course.objects.get_or_create(
        name=name,
        description=description,
        teacher=User.objects.get(username=teacher, profile__role='T'))[0]
    if students:
        for student in students:
            course.students.add(User.objects.get(username=student, profile__role='S'))
    course.save()
    return course
    

def add_exam(title, course, date_available, deadline, questions=None):
    exam = Exam.objects.get_or_create(
        title=title,
        course=Course.objects.get(name=course),
        date_available=date_available,
        deadline=deadline)[0]
    if questions:
        for question in questions:
            exam.questions.add(question)
    return exam


def add_question(content, choices, correct_answer):
    choice_0 = choices[0]
    choice_1 = choices[1]
    choice_2 = choices[2]
    choice_3 = choices[3]
    choice_4 = choices[4]
    question = Question.objects.get_or_create(
        content=content,
        choice_0=choice_0,
        choice_1=choice_1,
        choice_2=choice_2,
        choice_3=choice_3,
        choice_4=choice_4,
        correct_answer=correct_answer)[0]
    return question


def add_submission(exam, student, answers, score=0, max_score=0, percentage=0):
    submission = Submission.objects.get_or_create(
        exam=exam,
        student=student,
        score=score,
        max_score=max_score,
        percentage=percentage)[0]

    if answers:
        for answer in answers:
            submission.answers.add(answer)

    submission.score = len([a for a in answers if a.answer == a.question.correct_answer])
    submission.max_score = exam.questions.count()
    submission.percentage = round(submission.score / submission.max_score * 10000) / 100
    submission.save()

    return submission


def add_answer(question, answer):
    answer = Answer.objects.get_or_create(
        question=question,
        answer=answer)[0]
    return answer


if __name__ == "__main__":
    print('Starting Exam Network population script...')
    populate()
