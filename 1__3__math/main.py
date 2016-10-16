import re

'''
# Функция
def calc(str):
    digits_and_ops = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', ' ', '(', ')']

    lst = []
    tmp_str = ''
    for c in str:
        if c in digits_and_ops:
            tmp_str = tmp_str + c
        elif tmp_str and len(tmp_str) > 2:

            lst.append(tmp_str)
            tmp_str = ''
    lst.append(tmp_str)
    for s in lst:
        print(s, end=" = ")
        print(eval(s))
'''

my_str = " сложение: 1.5*(-3.00333),  (123---) для действительных чисел тоже работает  -0.29756 + 2.," \
       " -1 вычитание: -10 -(-1.8736), умножение: (-5) * 7, деление: 19.00001 / (-7), 2*2, -1-(-1)," \
       " много пробелов --> (222)   /  (333)"

# Нет проверки парности скобок, только простые выражения.
res = re.findall("[(\-]*\d*[\.]*\d+[)]*\s*[\+\-\*\/]\s*[(\-]*\d*[\.]*\d+[)]*", my_str)
print(res)
for expr in res:
        print(expr, end=" = ")
        print(eval(expr))  # Функция eval вычисляет выражение из строке.
