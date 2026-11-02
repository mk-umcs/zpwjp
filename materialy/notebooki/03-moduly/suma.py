import sys


def main():
    suma = 0.0
    try:
        for argument in sys.argv[1:]:
            suma += float(argument)
    except ValueError:
        print("Argumenty muszą być liczbami.")
    else:
        print(suma)


if __name__ == "__main__":
    main()
