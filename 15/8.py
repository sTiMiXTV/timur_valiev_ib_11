def month_name(n, lang):
    if lang == 'ru':
        return ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'][n - 1]
    if lang == 'en':
        return ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'][n - 1]
    return ''

print(month_name(3, "en"))
