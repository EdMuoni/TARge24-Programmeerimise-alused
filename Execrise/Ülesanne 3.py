"""
Koosta programm, mis aitab lastel treenida liitmist.
Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust.
Kui vastus on õige, kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte.
Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10),
samuti võib olla ette antud piirid, kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50).
Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse.
Näiteks:

Tere! Õpime arvutama. Esitan 10 liitmistehet, püüa vastata õigesti.
5 + 16 =
>> 21
Tubli, õige vastus!
18 + 23 =
>> 39
Sinu vastus polnud õige. Õige vastus on 41.
[...]
2 + 5 =
>> 7
Tubli, õige vastus!
See oli viimane ülesanne. Kogusid 10-st punktist 7.

Täiendusi vabal valikul:

Programm lubab kasutajal alguses sisestada, mitut tehet soovitakse.
Esitatavate arvude piirid saab kasutaja ette anda (maksimum või nii miinimum kui maksimum).
Küsitakse mitte ainult liitmistehteid, vaid ka teisi (lahutamine, korrutamine, jagamine).
Vastavalt lõpptulemusele reageeritakse erinevalt: "Ülihea!", "Olid tubli!",
"Korralik keskmine tulemus!", "Püüad järgmisel korral rohkem." vms.
"""

from random import randint

# Tee tsüklis
arv1 = randint(1, 50)
arv2 = randint(1, 50)

# Kontrolli vastuse korrektsust ja kiida või julgusta  vastavalt

# Hoia meeles mitu korda õigesti vastati ja teavita kasutajat programmi lõpus
count = 0


def show_equation(operation_symbol, correct_answer, first_number,
                  second_number):
    user_answer = int(
        input(f"{first_number} {operation_symbol} {second_number} = ? "))
    if user_answer == correct_answer:
        print("CORRECT! very smart!")
        return 1
    else:
        print(f"Room for improvement!")
        print(
            f"{first_number} {operation_symbol} {second_number} = {correct_answer}")
    return 0


def practice_adding(lowest=1, highest=50, count=10):
    correct_answers = 0
    for i in range(count):
        first_number = randint(lowest, highest)
        second_number = randint(lowest, highest)
        random_operator = randint(1, 3)
        if random_operator == 1:
            correct_answer = first_number + second_number
            correct_answers += show_equation("+", correct_answer, first_number,
                                             second_number)
        elif random_operator == 2:
            correct_answer = first_number - second_number
            correct_answers += show_equation("-", correct_answer, first_number,
                                             second_number)
        elif random_operator == 3:
            correct_answer = first_number * second_number
            correct_answers += show_equation("*", correct_answer, first_number,
                                             second_number)
    print(
        f"You tried {count} times and got the answer correct {correct_answers} times.")


if __name__ == '__main__':
    practice_adding()
    lowest = int(input("Sisesta väikseim täisarv, mida kasutada: "))
    highest = int(input("Sisesta suurim täisarv, mida kasutada: "))
    count = int(input("Sisesta tehete arv: "))
