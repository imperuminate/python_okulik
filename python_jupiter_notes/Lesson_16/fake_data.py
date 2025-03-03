from faker import Faker

fake_en = Faker()
fake_ru = Faker(locale="ru_RU")

print(fake_en.address())
print(fake_en.name())
print(fake_ru.address())
print(fake_ru.name())