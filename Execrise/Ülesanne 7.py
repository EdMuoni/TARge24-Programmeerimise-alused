"""
Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN.
Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d, näiteks:


X O O O O O O O X
O X O O O O O X O
O O X O O O X O O
O O O X O X O O O
O O O O X O O O O
O O O X O X O O O
O O X O O O X O O
O X O O O O O X O
X O O O O O O O X
... või (paarisarvulise N-i puhul):

X O O O O O O O O X
O X O O O O O O X O
O O X O O O O X O O
O O O X O O X O O O
O O O O X X O O O O
O O O O X X O O O O
O O O X O O X O O O
O O X O O O O X O O
O X O O O O O O X O
X O O O O O O O O X
Tühikuid võid lisada vastavalt oma soovile.

"""


def print_square(size):
    """
    Print a square with 0 times size.
    :param size:
    :return:
    """
    for row in range(size):
        for col in range(size):
            symbol = "0"
            if row == col or row + col + 1 == size:
                symbol = "X"
            print(f"{symbol}", end=" ")
        print()


# def print_square(size):
#     """
#     Print a square with 0 times size.
#     :param size:
#     :return:
#     """
#     for row in range(size):
#         for col in range(size):
#             print(f"0", end=" ")
#         print()


if __name__ == '__main__':
    size = int(input("Kui suurt ruutu soovid? "))
    print_square(size)
