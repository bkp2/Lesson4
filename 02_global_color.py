# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
def closed_figure(start_point, angle=0, step=90, length=100, color=(255, 255, 255)):
    point = sd.vector(start=start_point, angle=angle, length=length, color=color, width=1)
    for next_angle in range(step, 359, step):
        point = sd.vector(start=point, angle=angle+next_angle, length=length, color=color, width=1)
    sd.line(start_point=point, end_point=start_point, color=color, width=1)

def vector_triangle(start_point, angle, length, color):
    closed_figure(start_point=start_point, angle=angle, step=120, length=length, color=color)

def vector_square(start_point, angle, length, color):
    closed_figure(start_point=start_point, angle=angle, step=90, length=length, color=color)

def vector_pentagon(start_point, angle, length, color):
    closed_figure(start_point=start_point, angle=angle, step=72, length=length, color=color)

def vector_hexagon(start_point, angle, length, color):
    closed_figure(start_point=start_point, angle=angle, step=60, length=length, color=color)


palette = {'1': sd.COLOR_RED,
           '2': sd.COLOR_ORANGE,
           '3': sd.COLOR_YELLOW,
           '4': sd.COLOR_GREEN,
           '5': sd.COLOR_CYAN,
           '6': sd.COLOR_BLUE,
           '7': sd.COLOR_PURPLE}

while True:
    color = input(
        '1 - Red\n'
        '2 - Orange\n'
        '3 - Yellow\n'
        '4 - Green\n'
        '5 - Cyan\n'
        '6 - Blue\n'
        '7 - Purple\n'
        'Выберите номер цвета: ')

    if color in palette:
        point_0 = sd.random_point()
        point_1 = sd.random_point()
        point_2 = sd.random_point()
        point_3 = sd.random_point()

        vector_triangle(point_0, 90, 100, palette[color])
        vector_square(point_1, 90, 100, palette[color])
        vector_pentagon(point_2, 90, 100, palette[color])
        vector_hexagon(point_3, 90, 100, palette[color])
        break
    else:
        print('Неверный ввод!')
sd.pause()
