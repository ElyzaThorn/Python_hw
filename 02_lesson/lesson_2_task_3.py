import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area


print(square(4))
print(square(4.5))
print(square(5.1))
