from lab2_oop.rectangle import Rectangle
from lab2_oop.circle import Circle
from lab2_oop.square import Square

from colorama import Fore, Style, init


def main():
    init(autoreset=True)

    N = int(input("Введите номер вашего варианта N: "))

    rect = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")
    
    print(Fore.BLUE + str(rect) + Style.RESET_ALL)
    print(Fore.GREEN + str(circle) + Style.RESET_ALL)
    print(Fore.RED + str(square) + Style.RESET_ALL)


if __name__ == "__main__":
    main()
