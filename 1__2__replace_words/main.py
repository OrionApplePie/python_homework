# -*- coding: utf-8 -*-
import re

domains = (".com", ".org", ".net", ".gov", ".edu", ".ru", ".рф")


# Функция проверки на е-mail
def is_email(str_in, dom):
    # Если содержит собачку, то разложить в кортеж методом partition с шаблоном "@".
    if '@' in str_in:
        cort = str_in.partition("@")
        isdom = False
        # Проверка, окончивается ли строка каким-либо доменным именем из списка.
        for d in dom:
            isdom = cort[2].endswith(d)
            if isdom:
                domain = d
                break
        # Если это email, то возвр. True.
        if cort[0] != '' and cort[2] != '' and isdom and cort[2] != domain:
            return True
        else:
            return False
    else:  # Если нет @.
        return False


# Функция проверки на ссылку.
def is_link(str_in, dom):
    isdom = False
    for d in dom:
        isdom = str_in.endswith(d)
        if isdom:
            break
    if str_in.startswith("www."):
        return True
    else:
        return False


def my_func(str_in):
    # Разбиение строки на список слов (разделитель - пробел).
    words = str_in.split(' ')
    new_words = []
    for word in words:
        # В нижний регистр.
        tmp_word = word.lower()
        if is_email(tmp_word, domains):
            tmp_word = "[контакты запрещены]"
        elif is_link(tmp_word, domains):
            tmp_word = "[ссылка запрещена]"
        elif len(tmp_word) > 3 and tmp_word.isdigit():  # Строки-числа более 3 символов удаляются.
            tmp_word = ""
        if tmp_word:
            new_words.append(tmp_word)
    # Первое слово с заглавной буквы.
    new_words[0] = new_words[0].capitalize()
    # Список преобразован в строку.
    new_str = ' '.join(new_words)
    return new_str


my_str = "heLLO vasya@gmail.com COOL1234 www.cool.ru www.LinkOrNot ru STRING WORD" \
      " one www.google.com 1991 2016 42 133 00 qwerty admin@google.com BYE"

'''
print(my_func("http://www.google.ru"))
print(is_link(".com", domains))
print(is_email("aaa@.com", domains))
'''

# При помощи встроенных функций.
print(my_str)
res = my_func(my_str)
print(res)

# С помощью регулярных выражений.

# Замена всех букв верхнего регистра на нижний.
res = re.sub(r'\w+', lambda f: f.group(0).lower(), my_str)
# Установка 1-й буквы 1-го слова в верхний регистр.
res = re.sub(r'\w', lambda f: f.group(0).upper(), res, count=1)
# Замена емайлов.
res = re.sub(r'\w+@\w+.\w+', '[контакты запрещены]', res)
# Замена ссылок.
res = re.sub(r'www[\.]\w+[\.]*\w*', '[ссылка запрещена]', res)
# Удаление слов состоящих только из цифр и длиной более 3.
res = re.sub(r'\s\d\d\d\d+', '', res)
print(res)
