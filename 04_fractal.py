# -*- coding: utf-8 -*-

import simple_draw as sd
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви
# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
def draw_branches(start_point, angle, length):
    sd.vector(start=start_point, angle=angle-30, length=length, width=2)
    sd.vector(start=start_point, angle=angle+30, length=length, width=2)

def draw_branches_recursive(start_point, angle, length):
    if length < 5:
        return
    length *= 0.75
    v1 = sd.vector(start=start_point, angle=angle-30, length=length, width=1)
    v2 = sd.vector(start=start_point, angle=angle+30, length=length, width=1)
    draw_branches_recursive(v1, angle=angle-30, length=length)
    draw_branches_recursive(v2, angle=angle+30, length=length)

def draw_random_branches_recursive(start_point, angle, length):
    if length < 5:
        return

    v1 = sd.vector(start=start_point, angle=angle, length=length, width=1)
    random_length = length * (0.75 + 0.75 * sd.random_number(-20, 20) / 100)
    random_angle = 30 + 30 * sd.random_number(-40, 40) / 100.0
    draw_random_branches_recursive(v1, angle=angle - random_angle, length=random_length)

    random_length = length * (0.75 + 0.75 * sd.random_number(-20, 20) / 100)
    random_angle = 30 + 30 * sd.random_number(-40, 40) / 100.0
    draw_random_branches_recursive(v1, angle=angle + random_angle, length=random_length)

point0 = sd.get_point(300, 0)
draw_random_branches_recursive(point0, 90, 100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


