# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
def closed_figure(start_point, angle, step, length):
    point = sd.vector(start=start_point, angle=angle, length=length, width=1)
    for next_angle in range(step, 359, step):
        point = sd.vector(start=point, angle=angle+next_angle, length=length, width=1)
    sd.line(start_point=point, end_point=start_point, width=1)

def vector_triangle(start_point, angle, length):
    closed_figure(start_point=start_point, angle=angle, step=120, length=length)

def vector_square(start_point, angle, length):
    closed_figure(start_point=start_point, angle=angle, step=90, length=length)

def vector_pentagon(start_point, angle, length):
    closed_figure(start_point=start_point, angle=angle, step=72, length=length)

def vector_hexagon(start_point, angle, length):
    closed_figure(start_point=start_point, angle=angle, step=60, length=length)

point_0 = sd.random_point()
point_1 = sd.random_point()
point_2 = sd.random_point()
point_3 = sd.random_point()

# point_0 = sd.get_point(100, 100)
# point_1 = sd.get_point(200, 200)
# point_2 = sd.get_point(300, 300)
# point_3 = sd.get_point(400, 400)

vector_triangle(point_0, 90, 100)
vector_square(point_1, 90, 100)
vector_pentagon(point_2, 90, 100)
vector_hexagon(point_3, 90, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
