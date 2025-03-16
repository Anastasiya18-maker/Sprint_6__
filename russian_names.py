import random

class RussianNames:
    def __init__(self):
        self.male_names = [
            "Александр",
            "Дмитрий",
            "Сергей",
            "Андрей",
            "Максим"
        ]

        self.female_names = [
            "Анна",
            "Мария",
            "Екатерина",
            "Юлия",
            "Ольга"
        ]

        self.male_surname = [
            "Александров",
            "Дмитриев",
            "Сергеев",
            "Андреев",
            "Максимов"
        ]

        self.female_surname = [
            "Александрова",
            "Дмитриева",
            "Сергеева",
            "Андреева",
            "Максимова"
        ]


    def get_random_male_name(self):
        return random.choice(self.male_names)

    def get_random_female_name(self):
        return random.choice(self.female_names)

    def get_random_male_surname(self):
        return random.choice(self.male_surname)

    def get_random_female_surname(self):
        return random.choice(self.female_surname)

    def get_person(self):
        # Возвращает случайное полное имя.
        if random.choice([True, False]):
            return self.get_random_male_name() + ' ' + self.get_random_male_surname()
        else:
            return self.get_random_female_name()  + ' ' + self.get_random_female_surname()




