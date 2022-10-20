# Задача 1. Создайте файл. 
# Запишите в него N первых элементов последовательности Фибоначчи.

# 6 –> 1 1 2 3 5 8

def fibonacci():
    x = [0,1]
    i=2
    limit = int((input("Enter N: ")))
    while i <= limit:
        x.append(x[i-1]+x[i-2])
        i+=1
    str_fib = []
    for e in x:
        str_fib.append(str(e)+ ' ')
    return str_fib

def fib_writer():
    data = open('fibonacci.txt', 'w', encoding='utf-8')
    set_data = fibonacci()
    data.writelines(set_data)
    data.close()

fib_writer()


# Задача 2. В файле находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются на заданную букву.

# а –> абрикос, авокадо, апельсин, айва.

def print_fruits():
    data = open('fruits.txt', 'r', encoding='utf-8')
    fruits_list = data.readlines()
    data.close
    fruits_list = [line.rstrip() for line in fruits_list]
    letter = input("Enter letter: ")
    for word in fruits_list:
        if word.lower().startswith(letter):
            print(word)

print_fruits()

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

# «как тебя зовут?» –> меня зовут Анатолий


def bot():
    respond_dic = \
    {
        'привет' : 'Доброго времени суток, сэр',
        'как тебя зовут' : 'Люди зовут меня, Анатолий, сэр'
    }
    question = input("Спроси меня о чем угодно: ").lower()
    if question in respond_dic:
        print(respond_dic[question])

bot()