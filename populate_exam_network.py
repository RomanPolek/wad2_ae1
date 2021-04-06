import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wad2_ae1.settings')
import django

django.setup()

from django.contrib.auth.models import User
from exam_network.models import Profile
import datetime

def populate():
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
        "description":"20th century - events & inventions "},

        {"name":"Anatomy 1",
        "description":"Advanced course in Human Body"},

        {"name":"Computing Science 1",
        "description":"Advanced course in Algebra"},

        {"name":"English Literature",
        "description":"Advanced course in English Literature"},

        {"name":"Geography 2",
        "description":"Advanced course in Geography"}
        ]
    exams = [
        {"title":"Exam 1",
        "date_available": datetime.datetime(2021,3,20,9,0,0),
        "deadline":datetime.datetime(2021,3,21,0,0,0),
        "course":"Computing Science 1"},

        {"title":"Exam 1",
        "date_available": datetime.datetime(2021,3,28,13,15,0),
        "deadline":datetime.datetime(2021,3,29,23,30,0),
        "course":"History 2"},

        {"title":"Exam 1",
        "date_available": datetime.datetime(2021,5,18,11,0,0),
        "deadline":datetime.datetime(2021,5,19,0,0,0),
        "course":"Anatomy 1"},

        {"title":"Exam 2",
        "date_available": datetime.datetime(2021,5,12,12,0,0),
        "deadline":datetime.datetime(2021,5,13,0,0,0),
        "course":"Anatomy 1"},

        {"title":"Exam 1",
        "date_available": datetime.datetime(2021,5,8,11,30,0),
        "deadline":datetime.datetime(2021,5,9,0,0,0),
        "course":"Geography 2"}
        ]
    questions = [
        {"exam":0,
        "content":"Which of the following bit patterns represents the value 5?",
        "choice_1":"00010101",
        "choice_2":"00011100",
        "choice_3":"00000101",
        "choice_4":"00001101",
        "choice_5":"00001100",
        "correct_answer":2},

        {"exam":0,
        "content":"Which of the following bit patterns represents the value 15?",
        "choice_1":"00001111",
        "choice_2":"00001001",
        "choice_3":"00101001",
        "choice_4":"00111001",
        "choice_5":"00011101",
        "correct_answer":0},

        {"exam":0,
        "content":"Which of the following bit patterns represents the value 10?",
        "choice_1":"00001010",
        "choice_2":"10001010",
        "choice_3":"10101010",
        "choice_4":"00101010",
        "choice_5":"00001000",
        "correct_answer":0},

        {"exam":0,
        "content":"Which of the following bit patterns represents the value 100?",
        "choice_1":"01100111",
        "choice_2":"01111100",
        "choice_3":"01100111",
        "choice_4":"01111111",
        "choice_5":"01100100",
        "correct_answer":4},

        {"exam":0,
        "content":"Which of the following bit patterns represents the value 255?",
        "choice_1":"11100011",
        "choice_2":"11111110",
        "choice_3":"11111111",
        "choice_4":"11000110",
        "choice_5":"11010101",
        "correct_answer":2},

        {"exam":1,
        "content":"In which year did World War II start?",
        "choice_1":"1944",
        "choice_2":"1938",
        "choice_3":"1943",
        "choice_4":"1939",
        "choice_5":"1940",
        "correct_answer":3},

        {"exam":1,
        "content":"In which year did World War II end?",
        "choice_1":"1945",
        "choice_2":"1955",
        "choice_3":"1949",
        "choice_4":"1939",
        "choice_5":"1959",
        "correct_answer":0},

        {"exam":1,
        "content":"In which year was London due to host the Olympic Games, but couldn't because of the Second World War?",
        "choice_1":"1950",
        "choice_2":"1955",
        "choice_3":"1930",
        "choice_4":"1939",
        "choice_5":"1944",
        "correct_answer":4},

        {"exam":1,
        "content":"In which year the League of Nations was formed?",
        "choice_1":"1950",
        "choice_2":"1920",
        "choice_3":"1930",
        "choice_4":"1940",
        "choice_5":"1910",
        "correct_answer":1},

        {"exam":1,
        "content":"when did women cast their first vote in America?",
        "choice_1":"1915",
        "choice_2":"1929",
        "choice_3":"1919",
        "choice_4":"1910",
        "choice_5":"1920",
        "correct_answer":4},

        {"exam":2,
        "content":"Where is the pharynx located?",
        "choice_1":"neck",
        "choice_2":"head",
        "choice_3":"foot",
        "choice_4":"arm",
        "choice_5":"leg",
        "correct_answer":0},

        {"exam":2,
        "content":"Which of these glands produces tears?",
        "choice_1":"lattimmi",
        "choice_2":"lechamal",
        "choice_3":"fareal",
        "choice_4":"laryngeal",
        "choice_5":"lachrymal",
        "correct_answer":4},

        {"exam":2,
        "content":"Where is the esophagus located?",
        "choice_1":"chest",
        "choice_2":"head",
        "choice_3":"arm",
        "choice_4":"leg",
        "choice_5":"neck",
        "correct_answer":0},

        {"exam":2,
        "content":"What hormone, produced in the pancreas, regulates blood sugar levels?",
        "choice_1":"oxytocin",
        "choice_2":"epinephrine",
        "choice_3":"insulin",
        "choice_4":"prolactin",
        "choice_5":"serotonin",
        "correct_answer":2},

        {"exam":2,
        "content":"What is the name of the system in the human body that transports blood?",
        "choice_1":"cardiovascular",
        "choice_2":"lymphatic",
        "choice_3":"respiratory",
        "choice_4":"digestive",
        "choice_5":"endocrine",
        "correct_answer":0},

        {"exam":3,
        "content":"Which of these is a neurological disorder?",
        "choice_1":"alopecia",
        "choice_2":"psiatica",
        "choice_3":"Hashimoto syndrome",
        "choice_4":"Alzheimer disease",
        "choice_5":"ticapecia",
        "correct_answer":3},

        {"exam":3,
        "content":"Where are red blood corpuscles formed?",
        "choice_1":"bones",
        "choice_2":"heart",
        "choice_3":"lungs",
        "choice_4":"eyes",
        "choice_5":"nose",
        "correct_answer":0},

        {"exam":3,
        "content":"Where are red blood corpuscles formed?",
        "choice_1":"bones",
        "choice_2":"heart",
        "choice_3":"lungs",
        "choice_4":"eyes",
        "choice_5":"nose",
        "correct_answer":0},

        {"exam":3,
        "content":"What is the formation of new blood vessels called?",
        "choice_1":"Manugenesis",
        "choice_2":"Osteogenesis",
        "choice_3":"Catheterization",
        "choice_4":"Angiogenesis",
        "choice_5":"Angioterization",
        "correct_answer":3},

        {"exam":3,
        "content":"What separates the lobes of the lungs from one another?",
        "choice_1":"Tissure",
        "choice_2":"Hilum",
        "choice_3":"Trachea",
        "choice_4":"Pleura",
        "choice_5":"Fissure",
        "correct_answer":3},

        {"exam":4,
        "content":"What is the capital of Mozambique?",
        "choice_1":"Madrid",
        "choice_2":"Casablanca",
        "choice_3":"Maputo",
        "choice_4":"Kano",
        "choice_5":"Bangui",
        "correct_answer":2},

        {"exam":4,
        "content":"Which country is the chief home of the Shona people?",
        "choice_1":"Egypt",
        "choice_2":"Angola",
        "choice_3":"Namibia",
        "choice_4":"Kenya",
        "choice_5":"Zimbabwe",
        "correct_answer":4},

        {"exam":4,
        "content":"Serengeti National Park is in which country?",
        "choice_1":"Tanzania",
        "choice_2":"Mali",
        "choice_3":"Niger",
        "choice_4":"Botswana",
        "choice_5":"Sudan",
        "correct_answer":2},

        {"exam":4,
        "content":"Which country was formerly called Rhodesia?",
        "choice_1":"Zimbabwe",
        "choice_2":"Algeria",
        "choice_3":"Ghana",
        "choice_4":"Liberia",
        "choice_5":"Guinea",
        "correct_answer":2},

        {"exam":4,
        "content":"Which lake is the largest lake in Africa and the main reservoir of the Nile?",
        "choice_1":"Lake Victoria",
        "choice_2":"Lake Tanganyika",
        "choice_3":"Lake Sualiki",
        "choice_4":"Lake Gahauli",
        "choice_5":"Lake Guaru",
        "correct_answer":2}

        ]

    submission = [
        {"exam":0,
        "student":"o.nichols.9063@test.com",
        "score":12},

        {"exam":0,
        "student":"b.solomon.4258@test.com",
        "score":20},

        {"exam":0,
        "student":"k.parrish.5269@test.com",
        "score":16},

        {"exam":0,
        "student":"h.holman.5412@test.com",
        "score":4},

        {"exam":0,
        "student":"m.spencer.4173@test.com",
        "score":8},

        {"exam":0,
        "student":"a.bradley.5603@test.com",
        "score":16},

        {"exam":0,
        "student":"m.baldwin.3021@test.com",
        "score":20},

        {"exam":0,
        "student":"a.mullen.1045@test.com",
        "score":8},

        {"exam":0,
        "student":"a.carney.3026@test.com",
        "score":12},

        {"exam":0,
        "student":"d.beasley9875@test.com",
        "score":20},

        {"exam":1,
        "student":"o.nichols.9063@test.com",
        "score":12},

        {"exam":1,
        "student":"b.solomon.4258@test.com",
        "score":20},

        {"exam":1,
        "student":"h.holman.5412@test.com",
        "score":4},

        {"exam":1,
        "student":"m.spencer.4173@test.com",
        "score":8},

        {"exam":1,
        "student":"a.bradley.5603@test.com",
        "score":16},

        {"exam":1,
        "student":"a.mullen.1045@test.com",
        "score":8},

        {"exam":1,
        "student":"a.carney.3026@test.com",
        "score":12}

        ]
    answers = [
        {"question": 0,
        "answer":1,
        "results":0},

        {"question": 1,
        "answer":2,
        "results":0},

        {"question": 2,
        "answer":4,
        "results":0},

        {"question": 3,
        "answer":3,
        "results":0},

        {"question": 4,
        "answer":1,
        "results":0},

        {"question": 0,
        "answer":3,
        "results":1},

        {"question": 1,
        "answer":2,
        "results":1},

        {"question": 2,
        "answer":4,
        "results":1},

        {"question": 3,
        "answer":0,
        "results":1},

        {"question": 4,
        "answer":0,
        "results":1},

        {"question": 0,
        "answer":1,
        "results":2},

        {"question": 1,
        "answer":3,
        "results":2},

        {"question": 2,
        "answer":4,
        "results":2},

        {"question": 3,
        "answer":3,
        "results":2},

        {"question": 4,
        "answer":3,
        "results":2},

        {"question": 0,
        "answer":1,
        "results":3},

        {"question": 1,
        "answer":0,
        "results":3},

        {"question": 2,
        "answer":1,
        "results":3},

        {"question": 3,
        "answer":4,
        "results":3},

        {"question": 4,
        "answer":4,
        "results":3},

        {"question": 0,
        "answer":3,
        "results":4},

        {"question": 1,
        "answer":3,
        "results":4},

        {"question": 2,
        "answer":0,
        "results":4},

        {"question": 3,
        "answer":1,
        "results":4},

        {"question": 4,
        "answer":1,
        "results":4},

        {"question": 0,
        "answer":3,
        "results":5},

        {"question": 1,
        "answer":2,
        "results":5},

        {"question": 2,
        "answer":1,
        "results":5},

        {"question": 3,
        "answer":4,
        "results":5},

        {"question": 4,
        "answer":3,
        "results":5},

        {"question": 0,
        "answer":2,
        "results":6},

        {"question": 1,
        "answer":1,
        "results":6},

        {"question": 2,
        "answer":0,
        "results":6},

        {"question": 3,
        "answer":4,
        "results":6},

        {"question": 4,
        "answer":3,
        "results":6},

        {"question": 1,
        "answer":1,
        "results":7},

        {"question": 2,
        "answer":0,
        "results":7},

        {"question": 3,
        "answer":4,
        "results":7},

        {"question": 4,
        "answer":3,
        "results":7},

        {"question": 0,
        "answer":1,
        "results":8},

        {"question": 1,
        "answer":2,
        "results":8},

        {"question": 2,
        "answer":1,
        "results":8},

        {"question": 3,
        "answer":0,
        "results":8},

        {"question": 4,
        "answer":0,
        "results":8},

        {"question": 0,
        "answer":1,
        "results":9},

        {"question": 1,
        "answer":1,
        "results":9},

        {"question": 2,
        "answer":3,
        "results":9},

        {"question": 3,
        "answer":4,
        "results":9},

        {"question": 4,
        "answer":0,
        "results":9},

        {"question": 0,
        "answer":1,
        "results":10},

        {"question": 1,
        "answer":3,
        "results":10},

        {"question": 2,
        "answer":2,
        "results":10},

        {"question": 3,
        "answer":0,
        "results":10},

        {"question": 4,
        "answer":4,
        "results":10},

        {"question": 0,
        "answer":3,
        "results":11},

        {"question": 1,
        "answer":1,
        "results":11},

        {"question": 2,
        "answer":2,
        "results":11},

        {"question": 3,
        "answer":0,
        "results":11},

        {"question": 4,
        "answer":4,
        "results":11},

        {"question": 0,
        "answer":4,
        "results":12},

        {"question": 1,
        "answer":3,
        "results":12},

        {"question": 2,
        "answer":2,
        "results":12},

        {"question": 3,
        "answer":2,
        "results":12},

        {"question": 4,
        "answer":1,
        "results":12},

        {"question": 0,
        "answer":0,
        "results":13},

        {"question": 1,
        "answer":0,
        "results":13},

        {"question": 2,
        "answer":1,
        "results":13},

        {"question": 3,
        "answer":2,
        "results":13},

        {"question": 4,
        "answer":2,
        "results":13},

        {"question": 0,
        "answer":4,
        "results":14},

        {"question": 1,
        "answer":3,
        "results":14},

        {"question": 2,
        "answer":2,
        "results":14},

        {"question": 3,
        "answer":1,
        "results":14},

        {"question": 4,
        "answer":1,
        "results":14},

        {"question": 0,
        "answer":0,
        "results":15},

        {"question": 1,
        "answer":4,
        "results":15},

        {"question": 2,
        "answer":3,
        "results":15},

        {"question": 3,
        "answer":0,
        "results":15},

        {"question": 4,
        "answer":1,
        "results":15},

        {"question": 0,
        "answer":4,
        "results":16},

        {"question": 1,
        "answer":2,
        "results":16},

        {"question": 2,
        "answer":1,
        "results":16},

        {"question": 3,
        "answer":3,
        "results":16},
        ]


def add_user(first_name, last_name, email, password):
    user = User.objects.get_or_create(
        username=email,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password)[0]
    return user


def add_profile(user, role):
    profile = None
    try:
        profile = Profile.objects.get(user=user)
        profile.role = role
        profile.save()
    except Profile.DoesNotExist:
        profile = Profile.objects.get_or_create(
            user=user, role=role)[0]
    return profile


def add_course(name, description, teacher, students=None):
    course = Course.objects.get_or_create(
        name=name,
        description=description,
        teacher=teacher)[0]
    if students:
        for student in students:
            course.students.add(student)
    return course
    


def add_exam(title, course, date_available, deadline, questions=None):
    exam = Exam.objects.get_or_create(
        title=title,
        course=course,
        date_available=date_available,
        deadline=deadline)[0]
    if questions:
        for question in questions:
            exam.questions.add(question)
    return exam


def add_qustion(content, choices, correct_answer):
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


def add_submission(exam, student, score, max_score, percentage, answers):
    submission = Submission.objects.get_or_create(
        exam=exam,
        student=student,
        score=score,
        max_score=max_score,
        percentage=percentage)[0]
    if answers:
        for answer in answers:
            exam.questions.add(question)
    return submission


def add_answer(question, answer):
    answer = Answer.objects.get_or_create(
        question=question,
        answer=answer)[0]
    return answer


if __name__ == "__main__":
    print('Starting Exam Network population script...')
    populate()
