from datetime import date  # Модуль для преобр. формата даты
import urllib.request  # Модуль для открытия страницы
from xml.etree import ElementTree as etree  # API для работы с XML (парсить)


# Словарь с кодами валют.
# Данные берутся с сайта ЦБ РФ.
curr_codes = {"USD": "R01235", "EUR": "R01239", "JPY": "R01820", "GBP": "R01035",
              "AUD": "R01010", "DKK": "R01215", "CAD": "R01350", "SGD": "R01625"}

# Формирование сроки адреса с сегоднешней датой в формате dd/mm/YYYY
date = date.today().strftime("%d/%m/%Y")
str_url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req" + "=" + date

# Программа выполняется пока не введено 'x' или что-то еще кроме кодов валют
while True:
    print("Введите код валюты или 'x' для выхода")
    keys = curr_codes.keys()
    print(keys)
    print("----------------------------------------")
    currency_name = input()  # Ввод с клавиатуры
    currency_name = currency_name.upper()  # В верхний регистр
    if currency_name == 'X' or currency_name not in curr_codes:
        break
    my_valute_id = curr_codes[currency_name]  # Получение соотв. кода валюты

    # Функция urlopen возвращает объект со структурой xml,
    # а parse принимает и возвращает представление документа.
    currency = etree.parse(urllib.request.urlopen(str_url))

    # Метод findall ищет все дочерние элементы 'Value'(все валюты) в документе
    # и возвращает список,
    # далее проходимся и ищем валюту с нужным аттрибутом ID.
    for line in currency.findall('Valute'):
        id_val = line.get('ID')
        if id_val == my_valute_id:
            # Если найдено - то извлекаем курс(в руб.), наименование и номинал
            rub = line.find('Value').text
            name = line.find('Name').text
            nominal = line.find('Nominal').text

    # Вывод значений
    print("\nВалюта: " + nominal + " " + name)
    print("Курс: " + rub + " руб.")
    print("По данным ЦБ РФ")
    print("Дата: " + date)
    print("----------------------------------------")
