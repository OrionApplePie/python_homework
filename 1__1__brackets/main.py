

# функция для проверки правильности расположения скобок
def check_brackets(str):
    last_open = []  # список для хранения открывающих скобок из строки
    br_open = ['[',  '(',  '{']
    br_close = [']', ')', '}']
    count = 0  # счетчик скобок
    for c in str:  # проходимся по строке
        if c in br_open:  # собираем открывающие скобки в список и считаем их
            last_open.append(c)
            count += 1
        elif c in br_close:
            count += 1
            # на случай: ") aaa" или  "(a) [b] }" - т.е список откр. скобок - пуст, -
            # закр. скобка в самом начале, либо после всех закрытых парных скобок
            if not last_open:
                return count  # это ошибочная скобка - тогда функ. вернет номер этой скобки
            elif br_open.index(last_open.pop()) != br_close.index(c):
                # если попалась закрывающая скобка и список с собранным скобками не пуст,
                # то проверка на соответствие с последней открывающей скобке в last_open
                # в случае несоответствия - возврат номера скобки.
                # Используется метод pop - открывающая скобка автоматически удаляется из списка,
                # и на очереди уже предыдущая в списке(если есть)
                return count

    if not last_open:  # если все скобки правильно закрыты или их вообще нет в строке
        return "yes"
    else:  # если скобка\скобки не закрыты
        return -1


str1 = "^^^^ ---test (qwerty123 (tt[ first wrong bracket--> ) ] ( )rrr [qwerty {!!!@#$!@#$@! (*)} ] )) [][]  ([{ )"
str2 = "aaa ddd(aaa{bbb})  [cool [[!]777] cool] {{{!@#$%$#}}}"
str3 = "(WORD WORD WORD)"
str4 = "{{{{}}} NO CLOSED BRACKET"
str5 = "without brackets"
str6 = "( )( )( )( )( )( ] )( )( ))"
str7 = "f(1+5*(7-8*[123-21] ))"
str8 = "(cool ([ WRONG BRACKET ( #5 ] <--HERE ) ] )"
str9 = "ONLY CLOSE BR. }"
str10 = ",,,<<<{хахаха[] ](hi)"
test_strings = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10]

count = 1
for test_str in test_strings:
    res = check_brackets(test_str)
    print("string# ", count, " : ",  res)
    count += 1

'''
pattern = re.findall(r'\[\d+\]', str1)
print(pattern)
pattern2 = re.sub(r'\([^)]*$', "", str1)
print(pattern2)
'''
