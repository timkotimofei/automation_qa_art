from data.data import Person
from faker import Faker


faker_en = Faker('En')


# здесь мы вызывая generated_person мы вызываем класс  Person  из data.py с нашими полями

def generated_person():
    yield Person(
        full_name=faker_en.first_name() + ' ' + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.street_address(),
        permanent_address=faker_en.street_address(),
    )


# gen = next(generated_person())
#
# print(gen.permanent_address)