"""
Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
Täienda seda programmi nii, et kasutajalt küsitakse arve seni,
kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi.
Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
"""


def sum_ten_for():
    total = 0

    for number in range(1, 11):
        number = input("Palun sisesta number: ")
        total = total + int(number)
    print(f"Total sum is {total}")


def sum_ten_while():
    counter = 0
    total = 0

    while counter < 10:
        counter += 1
        total = total + counter
        user_number = int(input(f"Sisesta {counter}. täisarv: "))
        total += user_number
    print(f"Sisestatud arvude summa on {total}")


def sum_unlimited():
    counter = 0
    total = 0

    while True:  # TODO kirjuta õige tingimus
        counter += 1
        # TODO lahuta küsimine ja arvuks tegemine
        user_input = input(f"Sisesta {counter}. täisarv: ")
        if user_input == "":
            break
        user_number = int(user_input)
        total += user_number
        # TODO katkesta tsükkel teatud juhul
    print(f"Sisestatud arvude summa on {total}")


if __name__ == '__main__':
    sum_ten_for()
    sum_ten_while()
    sum_unlimited()
