profile_name = ''
profile_vacation_dates = ''

def setup_profile(name, vacation_dates):
    global profile_name, profile_vacation_dates
    profile_name = name
    profile_vacation_dates = vacation_dates

def print_application_for_leave():
    global profile_name, profile_vacation_dates
    print(f'Заявление на отпуск в период {profile_vacation_dates}. {profile_name}')

def print_holiday_money_claim(amount):
    global profile_name
    print(f'Прошу выплатить {amount} отпускных денег. {profile_name}')

def print_attorney_letter(to_whom):
    global profile_name, profile_vacation_dates
    print(f'На время отпуска в период {profile_vacation_dates} моим заместителем назначается {to_whom}. {profile_name}')

setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")
