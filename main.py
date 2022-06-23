# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5], dtype=np.float32)
#
# arr1 = np.random.randint(-100, 100, 500)
#
# print(arr1.mean())
#
# print(arr1.sum())
#
# arr3 = arr
# np.insert(arr, -1, 10)
#
# print(arr3 + arr)
#
#
# matix = np.random.random((3, 3))
#
# np.delete(matix, 0, axis=0)
#
# print(matix)
#
#
# print(np.info(np.eye))
#
#
# np.loadtxt('file.txt')
# np.genfromtxt('file.csv', delimiter=',')
#
# np.savetxt('file.txt', matix, delimiter=',')



# import numpy as np
# import matplotlib.pyplot as plt
# import math
# plt.style.use('seaborn-whitegrid')
#
# fig, ax = plt.subplots()
#
# def f(x):
#     return x**2
#
# a = float(input("a = "))
#
# x = [-4, -1, 0, 0, 1, 2, 3]
#
# y = []
#
# F = 0
# for i in x:
#     if i ** 2 - i < 1:
#         F = i ** 3 - 3 * i + 8
#     elif i ** 2 - i == 1:
#         F = 4 * f(i)
#     elif i ** 2 - i > 1:
#         F = 1 / (i ** 2 + 3 * i + 8)
#
#     y.append(F)
#
# ax.plot(x, y)
#
# plt.show()


# import matplotlib.pyplot as plt
# import math
# import numpy as np
# plt.style.use('seaborn-whitegrid')
# fig, ax = plt.subplots()
#
# x = [-3, -1, 0, 2, 6, 7]
# x_2 = [1, 2, 3, 4, 5, 6]
# y = []
#
# for i in x:
#     try:
#         y.append(math.sin(i) / (i + 2))
#     except ZeroDivisionError:
#         y.append(i)
#
# ax.plot(x, y, color='r', linestyle=':', label='y=(sinx)/(x+2)')
#
# ax.plot(x, y, color=(1.0, 0.2, 0.3), linestyle='--', label='y=(sinx)/(x+2)')
# ax.set_title("MATPLOTLIB", fontsize=20)
#
# ax.set_xlabel("Ось х")
# ax.set_ylabel("Ось y")
#
# # ax.legend(loc='lower left')
# ax.legend(loc='best')
#
# ax.grid(color='blue', lw=1, alpha=0.4)
#
# plt.show()


# --------------------------------------------------------------
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
#
# x = np.array([-3, -2, -1, 0, 1, 2, 3])
# y = np.array([9, 4, 1, 0, 1, 4, 9])
#
# ax.plot(x, y, marker="*", alpha=0.5, label='y=x^2')
#
# ax.plot(x, np.sin(x), color=(1.0, 0.2, 0.3), linestyle='--', label='y=sin(x)')
#
# ax.plot(x, np.cos(x), color='g', linestyle=':', label='y = cos(x)')
#
# ax.plot(x, x+5, 'o-r', lw=2.5, label='y = x + 5')
#
# ax.set_title("MATPLOTLIB", fontsize=20)
#
# ax.set_xlabel("Ось х")
# ax.set_ylabel("Ось y")
#
# # ax.legend(loc='lower left')
# ax.legend(loc='best')
#
# ax.set_xticks(np.arange(-3, 3, 0.5))
#
# ax.set_yticks(np.arange(0, 10, 2))
#
# ax.grid(color='blue', lw=1, alpha=0.4)
#
# fig.savefig("./figure1.png")
#
# plt.show()
#
#
# import matplotlib.image as mpimg
#
# img = mpimg.imread("./figure1.png")
# plt.grid()
# plt.imshow(img)

# ---------------------------------------------------------


# ------------------------------------------
# import numpy as np
#
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
#
# N = 50
#
# x = np.random.rand(N)
# y = np.random.rand(N)
#
# colors = np.random.rand(N)
#
# area = (np.random.rand(N) * 30) ** 2
#
# ax.scatter(x, y, s=area, c=colors, alpha=0.5, marker="*", cmap='viridis')
#
#
# plt.show()

# -------------------------------------

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np
# fig = plt.figure(figsize=(10, 6))
#
# ax = fig.add_subplot(111, projection='3d')
#
# N = 50
#
# x = np.random.rand(N)
# y = np.random.rand(N)
#
# colors = np.random.rand(N)
#
# area = (np.random.rand(N) * 30) ** 2
#
# ax.scatter(x, y, s=area, c=colors, alpha=0.5, marker="*", cmap='viridis')
#
# plt.show()

# ---------------------------------------

# bars
#
# import matplotlib.pyplot as plt
#
# fig, axes = plt.subplots(1, 2)
#
# axes[0].bar([1, 2, 3], [3, 4, 5], color='red', label='vertical bar', alpha=0.8)
#
# axes[1].barh([0.5, 1, 2, 5], [0, 1, 2, 3])
#
# axes[0].legend(loc='best')
#
# plt.show()

# ----------------------------------

# Stacked bar chart

# import matplotlib.pyplot as plt
# import numpy as np
#
# fig = plt.figure(figsize=(8, 5))
#
# rect1 = plt.bar(np.arange(5), np.arange(5)**2, width=0.5, color='lightblue')
#
# rect2 = plt.bar(np.arange(5), np.arange(5)*2, width=0.5, color='#1f77b4')
#
# labels=["A", "B", "C", "D", "E"]
#
#
# plt.legend((rect1[0], rect2[0]), ('Support', 'Freedom'))
#
# plt.show()

# -------------------------------------------

# hist u boxplot

# import matplotlib.pyplot as plt
# import numpy as np
#
# fig, ax = plt.subplots()
#
# np.random.seed(19680801)
#
# mu, sigma = 100, 15
#
# x = mu + sigma * np.random.randn(10000)
#
# ax.hist(x, 1000, density=True, facecolor='black', alpha=0.75)
#
# plt.show()

# ---------------------------------------

# Area Chart

# import matplotlib.pyplot as plt
# import numpy as np
#
# fig, ax = plt.subplots()
#
# x = np.arange(0, 100, 1)
#
# y = x * 2
#
# ax.fill_between(x, y, color='skyblue', alpha=0.2)
# ax.plot(x, y, color='Slateblue', alpha=0.6)
#
# plt.show()

# ----------------------------------

# Pie Chart

# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots(figsize=(8, 8))
#
# labels = '1', '2', '3', '4', '5', '6'
#
# user_1 = [10, 10, 10, 10, 10, 10]
#
# ax.pie(user_1, labels=labels, explode=(0, 0, 0, 0, 0, 0),
#        autopct='%1.1f%%', startangle=130, shadow=False)
#
# plt.show()


# -------------------------------------


# import matplotlib.pyplot as plt
#
# from matplotlib import cm
#
# import numpy as np
#
# fig = plt.figure()
#
# ax = fig.gca(projection='3d')
#
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#
# plt.show()

# ---------------------------------

# Time Series Plot

# import pandas as pd
#
# import matplotlib.pyplot as plt
#
# import numpy as np
#
# plt.figure(figsize=(8, 6))
#
# ts = pd.Series(np.random.randn(100),
#                index=pd.date_range('5/5/2021', periods=100))
#
# ts = ts.cumsum()
# ts.plot()
#
# plt.show()

# -------------------------------------



#
#
# from PIL import Image, ImageDraw
#
#
# im = Image.new('RGB', (500, 300), (0, 128, 0))
# draw = ImageDraw.Draw(im)
#
#
# draw.rectangle((200, 100, 300, 200), fill='red', outline=(255, 255, 255))
# im.save('draw-ellipse-rectangle-line.jpg', quality=95)


# import tkinter as tk
#
# window = tk.Tk()
#
# canvas = tk.Canvas(window, bg="white", width=800, height=800)
#
# canvas.pack()
#
# canvas.create_oval((50, 80, 300, 300), fill="red")
#
# # canvas.create_arc((50, 100, 100, 150), extent=180, fill="black")
# #
# # canvas.create_arc((200, 100, 250, 150), extent=180, fill="black")
#
# canvas.create_line((100, 30, 150, 90), fill="green", width=10)
#
# # canvas.create_line((110, 240, 190, 240), fill="red", width=5)
# # canvas.create_line((190, 240, 250, 200), fill="red", width=5)
#
# window.mainloop()


# import turtle
#
# turtle.penup()
# for i in range(1, 500, 50):
#     turtle.right(90)    # Face South
#     turtle.forward(i)   # Move one radius
#     turtle.right(270)   # Back to start heading
#     turtle.pendown()    # Put the pen back down
#     turtle.circle(i)    # Draw a circle
#     turtle.color('red')
#     turtle.penup()      # Pen up while we go home
#     turtle.home()


# import turtle
# import math
#
# def drawHouse(t, length):
#     for i in range(4):
#         t.forward(length)
#         t.right(90)
#     t.left(45)
#     t.forward(length / math.sqrt(2))
#     t.right(90)
#     t.forward(length / math.sqrt(2))
#     t.right(135)
#     t.forward(length)
#
# window = turtle.Screen()
#
# pencil = turtle.Turtle()
#
# pencil.pensize(2)
#
# drawHouse(pencil, 150)
#
# window.exitonclick()


# from random import randint
#
# M = int(input("M = "))
#
# N = int(input("N = "))
#
# arr = [[randint(1, 10) for j in range(N)] for i in range(M)]
#
# print("Генерацияланган массив: ")
#
# for i in range(M):
#     print(arr[i])
#
# print("===================================")
#
# for i in range(N):
#     mult = 1
#     for j in range(M):
#         mult *= arr[j][i]
#
#     print(f"{i} бағанындағы элементтердің көбейтіндіcі: {mult}")


# Создайте структуру с именем train, содержащую поля: название
# пункта назначения, номер поезда, время отправления. Ввести
# данные в массив из пяти элементов типа train, упорядочить
# элементы по номерам поездов. Добавить возможность вывода
# информации о поезде, номер которого введен пользователем


# class train:
#
#     punct_name = None
#     number_of_train = None
#     time_of_going = None
#
#     def __init__(self,punct_name, number_of_train, time_of_going):
#         self.number_of_train = number_of_train
#         self.time_of_going = time_of_going
#         self.punct_name = punct_name
#
#     def get_inf(self):
#         print(f"Номер поезда: {self.number_of_train}\n"
#               f"Пункт назначения: {self.punct_name}\n"
#               f"Время отправления: {self.time_of_going}")
#
#
# mas = [train("Астана", 63, "12:00"), train("Алматы", 501, "19:00"), train("Шымкент", 89, "15:30")]
#
# mas = sorted(mas, key=lambda x: x.number_of_train, reverse=False)
#
# mas[0].get_inf()


# . Создать модуль с функциями:
#  1) функция которая добавляет в файл какой-то текст(текст спросить у
# пользователя)
#  2) Функция которая создает пустой файл
#  3) функция которая считает количество строк в нужном файле
# (спросить у пользователя имя файла)


# class file_class:
#     file_name = None
#
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def input_text(self, text):
#         f = open(self.file_name, "a")
#         f.write(text)
#         f.close()
#
#     def create_a_new_file(self):
#         f = open(self.file_name, "w")
#         f.close()
#
#     def count_a_num_of_line(self):
#         print(sum(1 for line in open(self.file_name, 'r')))
#         return sum(1 for line in open(self.file_name, 'r'))
#
#
# a = file_class("text.txt")
#
# a.create_a_new_file()
#
# a.input_text(" Создать модуль с функциями:\n"
#              "1) функция которая добавляет в файл какой-то текст(текст спросить у\n"
#              "пользователя)\n"
#              "2) Функция которая создает пустой файл\n"
#              "3) функция которая считает количество строк в нужном файле\n"
#              "(спросить у пользователя имя файла)\n"
#              )
#
# a.count_a_num_of_line()


# Класс Абонент: Идентификационный номер, Фамилия, Имя, Отчество,
# Адрес, Номер кредитной карточки, Дебет, Кредит, Время междугородных
# и городских переговоров; Конструктор;
# Методы: установка значений атрибутов, получение значений атрибутов,
# вывод информации.
# Создать массив объектов данного класса.
# Вывести сведения относительно абонентов, у которых время городских
# переговоров превышает заданное. Сведения относительно абонентов,
# которые пользовались междугородной связью.
# Список абонентов в алфавитном порядке.


# class abonent:
#     id = None
#     second_name = None
#     first_name = None
#     middle_name = None
#     address = None
#     num_of_card = None
#     debit = None
#     credit = None
#     time_of_long_distance_and_city_negotiations = None
#
#     def __init__(self, id, second_name, first_name, middle_name, address, num_of_card, debit, credit,
#                  time_of_long_distance_and_city_negotiations):
#         self.id = id
#         self.second_name = second_name
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.address = address
#         self.num_of_card = num_of_card
#         self.debit = debit
#         self.credit = credit
#         self.time_of_long_distance_and_city_negotiations = time_of_long_distance_and_city_negotiations
#
#     def output_inf(self):
#         print(f"id: {self.id}\n"
#               f"Фамилия: {self.second_name}\n"
#               f"Имя: {self.first_name}\n"
#               f"Отчество: {self.middle_name}\n"
#               f"Адрес: {self.address}\n"
#               f"Номер кредитной карты: {self.num_of_card}\n"
#               f"Дебет: {self.debit}\n"
#               f"Кредит: {self.credit}\n"
#               f"Время междугородных и городских переговоров: {self.time_of_long_distance_and_city_negotiations}\n")
#
#
# chel = abonent("0001", "Михаилов", "Андрей", "Петрович", "Пушкина 7", "1010 4564 4415 2179", "1234", "1 105 542 тг",
#                "0.048 сек")
#
# chel.output_inf()


# Составить описание класса для представления времени.
# Методы класса должны иметь функции установки времени
# и изменения его отдельных полей (час, минута, секунда) с
# проверкой допустимости вводимых значений(например
# меньше нуля и больше 60 секунд). В случае недопустимых
# значений изменять поля на ноль. Создать методы изменения
# времени на заданное количество часов, минут и секунд


# import datetime

# class time_now:
#     hour = None
#     minute = None
#     sec = None
#
#     def __init__(self, hour, minute, sec):
#         self.hour = hour
#         self.minute = minute
#         self.sec = sec
#
#     def change_hour(self, new_hour):
#         if int(new_hour) < 0 or int(new_hour) >= 24:
#             self.hour = '0'
#         else:
#             self.hour = new_hour
#
#     def change_minute(self, new_minute):
#         if int(new_minute) < 0 or int(new_minute) >= 60:
#             self.minute = '0'
#         else:
#             self.minute = new_minute
#
#     def change_sec(self, new_sec):
#         if int(new_sec) < 0 or int(new_sec) >= 60:
#             self.sec = '0'
#         else:
#             self.sec = new_sec
#
#     def print_time(self):
#         if len(str(self.hour)) == 1:
#             self.hour = "0" + str(self.hour)
#         if len(str(self.minute)) == 1:
#             self.minute = "0" + str(self.minute)
#         if len(str(self.sec)) == 1:
#             self.sec = "0" + str(self.sec)
#         print(f"{self.hour}:{self.minute}:{self.sec}")
#
# hour = datetime.datetime.now().hour
# minute = datetime.datetime.now().minute
# sec = round(datetime.datetime.now().second)
#
# t = time_now(hour, minute, sec)
# t.print_time()






# import matplotlib.pyplot as plt
# import math
# plt.style.use('seaborn-whitegrid')
#
# fig, ax = plt.subplots()
#
# def f(x):
#     return math.cos(x)
# x = [-3, -1, 0, 0, 1, 2, 5]
# y = []
# for i in x:
#     try:
#         y.append((i + 4)/(i - 1))
#     except ZeroDivisionError:
#         y.append(i)
#
# ax.plot(x, y)
#
#
# plt.show()

# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(sum(digits[1:4]))


