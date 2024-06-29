import datetime

day,mounth,year = map(int, input('Введите свою дату рождения: ').split('.'))

def calculate_age(year, mounth, day):
    birthday = datetime.date(year, mounth, day)
    today = datetime.date.today()
    if birthday.year <= today.year:
        age = today.year - birthday.year
        if birthday.month >= today.month:
            age -= 1
            if birthday.day <= today.day:
                age +=1

    return age

print(f'Ваш возраст: {calculate_age(year, mounth, day)}')




