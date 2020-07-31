import datetime


today = datetime.date.today()
Year = today.year
birthday = datetime.date(Year, int(input("Введите месяц вашего рождения")), int(input("Введите день вашего рождения")))
delta = birthday - today
nextYear = delta.days

if today == birthday:
    print("Happy Birthday!")
else:
    if nextYear < 0:
        nextYear += 365
    print("До вашего дня рождения " + str(nextYear) + " дней")