import math


def square(s):

    t = s * s
    print(f"площадь квадрата = {math.ceil(t)}")


square(float(input("введите сторону квадрата: ")))
