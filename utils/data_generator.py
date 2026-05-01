from faker import Faker
fake = Faker("zh_CN")

class DataGenerator:
    @staticmethod
    def username(): return fake.user_name()
    @staticmethod
    def phone(): return fake.phone_number()