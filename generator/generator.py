from faker.generator import random
import os
from data.data import Person, Color
from faker import Faker


faker_en = Faker('En')


# здесь мы вызывая generated_person мы вызываем класс  Person  из data.py с нашими полями
# Важно в реальном проекте в некоторых случаях я бы тянул эти данные из базы данных
def generated_person():
    yield Person(
        full_name=faker_en.first_name() + ' ' + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        age=random.randint(10,90),
        salary=random.randint(5000, 15000),
        department=faker_en.job(),
        current_address=faker_en.street_address(),
        permanent_address=faker_en.street_address(),
        mobile=faker_en.msisdn(),
        date_of_birth = faker_en.date_of_birth(None,20, 30)
    )


# gen = next(generated_person())
# print(gen.date_of_birth)
# print(str(gen.date_of_birth))



def generated_file():
    # path = f'/Users/timofeitimko/PycharmProjects/automation_qa_art/filetest{random.randint(1,999)}.txt'
    current_directory = os.getcwd()
    path = f'{current_directory}/filetest{random.randint(1,999)}.txt'
    with open(path, 'w+') as file:
        data = file.write('Hello World !')
    return file.name, path

# print(generated_file())
#
#
# current_directory = os.getcwd()
# print("Текущая директория:", current_directory)




def generate_subject():
    subjects_dict = {
        1: "Hindi",
        2: "English",
        3: "Maths",
        4: "Physics",
        5: "Chemistry",
        6: "Biology",
        7: "Computer Science",
        8: "Commerce",
        9: "Accounting",
        10: "Economics",
        11: "Arts",
        12: "Social Studies",
        13: "History",
        14: "Civics"
    }
    return subjects_dict[random.randint(1,14)]

# print(generate_subject())


def generate_state():
    state = {
        1: "NCR",
        2: "Uttar Pradesh",
        3: "Haryana",
        4: "Rajasthan",
    }
    return state[random.randint(1,4)]

# print(generate_state())


def generate_city(state):
    city = {
        "NCR": {
            1: "Delhi",
            2: "Gurgaon",
            3: "Noida"
        },
        "Uttar Pradesh": {
            1: "Agra",
            2: "Lucknow",
            3: "Merrut"
        },
        "Haryana": {
            1: "Karnal",
            2: "Panipat"
        },
        "Rajasthan": {
            1: "Jaipur",
            2: "Jaiselmer"
        }
    }
    return city[state][random.randint(1,2)]

# print(generate_city("Uttar Pradesh"))py


def generate_color():
    colors= {
        1: "Blue",
        2: "Green",
        3: "Yellow",
        4: "Purple",
        5: "Black",
        6: "White",
        7: "Voilet",
        8: "Indigo",
        9: "Magenta",
        10: "Aqua"
        }

    return colors[random.randint(1,10)]

# print(generate_color())
# col = {generate_color() for i in range(1,7)}
# print(col)


def true_generator_color(num):
    color_name = ["Red", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    color_name = random.sample(color_name,num)
    for i in color_name:
        yield i

# debug_gen = true_generator_color(3)
# print(next(debug_gen))
# print(next(debug_gen))
# print(next(debug_gen))









