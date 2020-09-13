# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rnd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

points = []
for point in range(N):
    points.append(sd.get_point(sd.random_number(0, 600), 600))
    # print(snowflakes[snowflake])
x, y = sd.random_number(0, 600), 600

lengths = []
for length in range(N):
    lengths.append(sd.random_number(10, 100))

while True:
    # sd.clear_screen()
    sd.start_drawing()
    for snowflake in range(N):
        center = points[snowflake]
        length = lengths[snowflake]
        sd.snowflake(center=center, length=length, color=sd.background_color)
        points[snowflake].y -= sd.random_number(1, 10)
        points[snowflake].x += sd.random_number(-10, 10)
        sd.snowflake(center=center, length=length, color=sd.COLOR_WHITE)
        if points[snowflake].y < 1:
            points[snowflake].y = 600

    sd.finish_drawing()
    sd.sleep(0.1)

    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


