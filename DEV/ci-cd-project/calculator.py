
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Dalīt ar nulli nedrīkst!")
    return a / b


def main():
    print("=== TERMINĀLA KALKULATORS ===")
    print("1 - Saskaitīšana")
    print("2 - Atņemšana")
    print("3 - Reizināšana")
    print("4 - Dalīšana")

    choice = input("Izvēlies darbību: ")

    try:
        a = float(input("Ievadi pirmo skaitli: "))
        b = float(input("Ievadi otro skaitli: "))

        operations = {
            "1": add,
            "2": subtract,
            "3": multiply,
            "4": divide
        }

        if choice not in operations:
            print("Nederīga izvēle!")
            return

        print("Rezultāts:", operations[choice](a, b))

    except ValueError as error:
        print("Kļūda:", error)


if __name__ == "__main__":
    main()
