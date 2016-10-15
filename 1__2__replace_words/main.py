# -*- coding: utf-8 -*-
import re

domains = (".com", ".org", ".net", ".gov", ".edu", ".ru", ".рф")


# функ. проверки на е-mail
def is_email(str, dom):
    if '@' in str:  # если содержит собачку, то разложить в кортеж методом partition с шаблоном "@"
        cort = str.partition("@")
        isdom = False
        for d in dom:  # проверяет, окончивается ли строка каким-либо доменным именем из списка
            isdom = cort[2].endswith(d)
            if isdom:
                domain = d
                break
        # если это email, то возвр. истину
        if cort[0] != '' and cort[2] != '' and isdom and cort[2] != domain:
            return True
        else:
            return False
    else:  # если нет @
        return False


# функ. проверки на ссылку
def is_link(str, dom):
    isdom = False
    for d in dom:
        isdom = str.endswith(d)
        domain = d
        if isdom:
            break
    if str.startswith("www."):
        return True
    else:
        return False
    '''
    elif (isdom and str != domain):  # or???
        return True
    '''


def my_func(str):
    words = str.split(' ')  # разбиение строки на список строк (разделитель - пробел)
    new_words = []
    for word in words:
        tmp_word = word.lower()  # в нижний рег.
        if is_email(tmp_word, domains):  # проверка на эмайл
            tmp_word = "[контакты запрещены]"
        elif is_link(tmp_word, domains):  # проверка на ссылку
            tmp_word = "[ссылка запрещена]"
        elif len(tmp_word) > 3 and tmp_word.isdigit():  # строки-числа более 3 символов удаляются
            tmp_word = ""
        if tmp_word:
            new_words.append(tmp_word)
    new_words[0] = new_words[0].capitalize()  # первое слово с заглавной буквы
    new_str = ' '.join(new_words)  # список преобр. в строку
    return new_str


str = "heLLO vasya@gmail.com COOL1234 www.cool.ru www.linkornot ru STRING WORD" \
      " one www.google.com 1991 2016 42 133 00 qwerty admin@google.com BYE"

'''
print(my_func("http://www.google.ru"))
print(is_link(".com", domains))
print(is_email("aaa@.com", domains))
'''

# при помощи встроенных функций
print(str)
res = my_func(str)
print(res)

# с помощью регулярных  выражений
res = re.sub(r'\w+', lambda f: f.group(0).lower(), str)  # замена всех букв вернего регистра на нижний
res = re.sub(r'\w', lambda f: f.group(0).upper(), res, count=1)  # установка 1-й буквы 1-го слова в верхний регистр
res = re.sub(r'\w+@\w+.\w+', '[контакты запрещены]', res)  # замена емайлов
res = re.sub(r'www[\.]\w+[\.]*\w*', '[ссылка запрещена]', res)  # замена ссылок
res = re.sub(r'\s\d\d\d\d+', '', res)  # удаление слов состоящих только из цифр и длиной более 3
print(res)
