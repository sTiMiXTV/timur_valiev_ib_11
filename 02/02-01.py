city_name_one = input('Enter your city name: ')
city_name_two = input('Enter your city name: ')
if city_name_one == "Тула" and city_name_two != "Пенза" and city_name_two != "Тула":
    print('ДА')
elif city_name_one != "Тула" and city_name_two == "Пенза" and city_name_two != "Тула":
    print("ДА")
else: print("НЕТ")