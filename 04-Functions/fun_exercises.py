"""Function examples."""


def func():
    """Print to console - I'm inside the function."""
    print("I'm inside the function")


def my_name_is(name: str) -> None:
    """
    Print to console - My name is [name].

    :param name: name you want to use
    """
    print(f"My name is {name}")


def sum_six(num):
    num = int(num)
    return num + 6


def sum_numbers(a, b):
    a = int(a)
    b = int(b)
    return a + b


def usd_to_eur(amount_usd):
    """Funktsioon töötab nii, et kui sisendiks on rahasumma dollarites, tagastab funktsioon summa eurodes."""
    exchange_rate = 0.80
    amount_eur = amount_usd * exchange_rate
    return amount_eur


if __name__ == '__main__':
    func()
    my_name_is("Edgar")
    my_name_is("Toomas")
    print(sum_six(1))  # --> 7
    print(sum_six(6))  # --> 12
    print(sum_numbers(5, 5))  # --> 10
    print(sum_numbers(0, 25))  # --> 25
    print(usd_to_eur(100))  # --> 80
