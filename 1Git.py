# Анализ сложности алкоритма

# Счеетчик уникальных символов в строке
# на вход функции строка. И функция считает, сколько раз в строке встретился каждый из символов

# Создаем функщию для подсчета уникальных символов
import time

def letterCount(line):
    for latter in set(line):   # set - функция, возвращающая множество(тип данных, в котором нет повторяющихся элементов)
        counter = 0
        # counter - счетчик, сколько раз встретился символ в строке
        for nextlatter in line:
            if latter == nextlatter:
                counter += 1
        print(latter, counter)

# замеряем время выполнения программы
start = time.time()
letterCount('abcdfgh' * 1000000)

# line = 'aaabbbcccddd'  # пример как работает множество(set)
# print(set(line))   

print(time.time() - start)