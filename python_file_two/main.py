import math

print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Вычисляем дискриминант
discriminant = b**2 - 4*a*c

if discriminant > 0:
    # Уравнение имеет два корня
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    # Уравнение имеет один корень
    x = -b / (2*a)
    print(f"Уравнение имеет один корень: x = {x}")
else:
    # Уравнение не имеет действительных корней
    print("Уравнение не имеет действительных корней")