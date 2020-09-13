# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
def closed_figure(start_point, angle=0, step=90, length=100, color=(255, 255, 255)):
    point = sd.vector(start=start_point, angle=angle, length=length, color=color, width=1)
    for next_angle in range(step, 359, step):
        point = sd.vector(start=point, angle=angle+next_angle, length=length, color=color, width=1)
    sd.line(start_point=point, end_point=start_point, color=color, width=1)

def vector_triangle(start_point, angle, length, color=(255, 255, 255)):
    closed_figure(start_point=start_point, angle=angle, step=120, length=length, color=color)

def vector_square(start_point, angle, length, color=(255, 255, 255)):
    closed_figure(start_point=start_point, angle=angle, step=90, length=length, color=color)

def vector_pentagon(start_point, angle, length, color=(255, 255, 255)):
    closed_figure(start_point=start_point, angle=angle, step=72, length=length, color=color)

def vector_hexagon(start_point, angle, length, color=(255, 255, 255)):
    closed_figure(start_point=start_point, angle=angle, step=60, length=length, color=color)


figures = {'1': 'triangle',
           '2': 'square',
           '3': 'pentagon',
           '4': 'hexagon',}

while True:
    figure = input(
        '1 - Треугольник\n'
        '2 - Квадрат\n'
        '3 - Пятиугольник\n'
        '4 - Шестиугольник\n'
        'Выберите номер фигуры: ')

    if figure in figures:
        point_0 = sd.get_point(300,300)

        if figure == '1':
            vector_triangle(point_0, 90, 100)
        elif figure == '2':
            vector_square(point_0, 90, 100)
        elif figure == '3':
            vector_pentagon(point_0, 90, 100)
        else:
            vector_hexagon(point_0, 90, 100)
        break
    else:
        print('Неверный ввод!')
sd.pause()
