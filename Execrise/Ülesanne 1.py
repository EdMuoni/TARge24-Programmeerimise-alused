"""
Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5 korda
ja lisab ka tervituse järjekorranumber.
"""


def solution():
    name = input("Palun siseta oma nimi: ")
    for i in range(5):
        print(f"Ole tervitatus, {name}, {i + 1}. korda")


if __name__ == "__main__":
    solution()
