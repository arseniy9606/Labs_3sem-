import sys
import math


class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            return None

        if self.a == 0:
            if self.b == 0:
                return []
            t = -self.c / self.b
            if t < 0:
                return []
            if t == 0:
                return [0.0]
            r = math.sqrt(t)
            return sorted([-r, r])

        D = self.discriminant()
        roots = []

        if D < 0:
            return []

        elif D == 0:
            t = -self.b / (2 * self.a)
            if t > 0:
                r = math.sqrt(t)
                roots.extend([-r, r])
            elif t == 0:
                roots.append(0.0)

        else:
            sqrtD = math.sqrt(D)
            t1 = (-self.b + sqrtD) / (2 * self.a)
            t2 = (-self.b - sqrtD) / (2 * self.a)

            for t in (t1, t2):
                if t > 0:
                    r = math.sqrt(t)
                    roots.extend([-r, r])
                elif t == 0:
                    roots.append(0.0)

        roots = list(set(roots))
        roots.sort()
        return roots

    
    def __str__(self):
        return f"{self.a} * x^4 + {self.b} * x^2 + {self.c} = 0"

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


def main():
    args = sys.argv[1:]

    cli_A = args[0] if len(args) > 0 else None
    cli_B = args[1] if len(args) > 1 else None
    cli_C = args[2] if len(args) > 2 else None

    A = read_coefficient("A", cli_A)
    B = read_coefficient("B", cli_B)
    C = read_coefficient("C", cli_C)

    equation = BiquadraticEquation(A, B, C)

    print("Решаем уравнение:", equation)

    D = equation.discriminant()
    if D is not None:
        print(f"Дискриминант относительно t = x^2: D = {D}")
    else:
        print("Коэффициент A = 0, дискриминант не вычисляется (уравнение не биквадратное).")

    roots = equation.solve()

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
