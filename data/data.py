from dataclasses import dataclass

# здесь создадим универсальный data класс, чтобы его сделать дата классом прописываем декратор @dataclasses
# необходимо строго прописывать тип этих свойств


@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    age: int = None
    salary: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None
    date_of_birth: str = None