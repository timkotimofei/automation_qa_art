from dataclasses import dataclass

# здесь создадим универсальный data класс, чтобы его сделать дата классом прописываем декратор @dataclasses
# необходимо строго прописывать тип этих свойств


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None