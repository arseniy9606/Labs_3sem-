import sys
import math


def read_coefficient(name, cli_value):
    while True:
        if cli_value is not None:
            text = cli_value
            cli_value = None
        else:
            text = input(f"Введите коэффициент {name}: ")

        try:
            value = float(text)
            return value
        except ValueError:
            print(f"Ошибка: коэффициент {name} должен быть действительным числом.")


def solve_biquadratic(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return None

    if a == 0:
        if b == 0:
            return []
        t = -c / b
        if t < 0:
            return []
        if t == 0:
            return [0.0]
        r = math.sqrt(t)
        return sorted([-r, r])

    D = b*b - 4*a*c
    roots = []

    if D < 0:
        return []

    elif D == 0:
        t = -b / (2*a)
        if t > 0:
            r = math.sqrt(t)
            roots.extend([-r, r])
        elif t == 0:
            roots.append(0.0)

    else:
        sqrtD = math.sqrt(D)
        t1 = (-b + sqrtD) / (2*a)
        t2 = (-b - sqrtD) / (2*a)
        for t in (t1, t2):
            if t > 0:
                r = math.sqrt(t)
                roots.extend([-r, r])
            elif t == 0:
                roots.append(0.0)

    roots = list(set(roots))
    roots.sort()
    return roots


def main():
    args = sys.argv[1:]
    cli_A = args[0] if len(args) > 0 else None
    cli_B = args[1] if len(args) > 1 else None
    cli_C = args[2] if len(args) > 2 else None

    A = read_coefficient("A", cli_A)
    B = read_coefficient("B", cli_B)
    C = read_coefficient("C", cli_C)

    print(f"Решаем уравнение: {A} * x^4 + {B} * x^2 + {C} = 0")

    if A != 0:
        D = B * B - 4 * A * C
        print(f"Дискриминант относительно t = x^2: D = {D}")
    else:
        print("Коэффициент A = 0, решаем упрощённое уравнение (дискриминант не вычисляется).")
    roots = solve_biquadratic(A, B, C)

    if roots is None:
        print("Уравнение тождественно 0 = 0, бесконечно много решений.")
        return

    if not roots:
        print("Действительных корней нет.")
    else:
        print("Действительные корни уравнения:")
        for idx, r in enumerate(roots, start=1):
            print(f"x{idx} = {r}")


if __name__ == "__main__":
    main()
