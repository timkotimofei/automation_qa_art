from faker.generator import random
import os
from data.data import Person
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
    )


# gen = next(generated_person())
#
# print(gen.first_name)


def generated_file():
    path = f'/Users/timofeitimko/PycharmProjects/automation_qa_art/filetest{random.randint(1,999)}.txt'
    with open(path, 'w+') as file:
        data = file.write('Hello World !')
    return file.name, path






