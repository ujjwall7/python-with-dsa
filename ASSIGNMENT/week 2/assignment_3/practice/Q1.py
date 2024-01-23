def helloWorld(num: int | None = None) -> int:
    i = 1
    if num != None:
        while i <= num:
            print("Hello world")
            i += 1
    else:
        return print(None)
# helloWorld()


def oneToNum(num: int = 1) -> int:
    i = 1
    while i <= 10:
        print(f"{i}", end=" ")
        i += 1
# oneToNum(10)


def Number(n: int = 0, m: int = 0) -> int:
    n_number = n
    m_number = m

    if n_number <= m_number:
        while n_number <= m_number:
            print(f"{n_number}", end=" ")
            n_number += 1

    if n_number >= m_number:
        n_number = m
        m_number = n
        while n_number <= m_number:
            print(f"{n_number}", end=" ")
            n_number += 1
# Number(43,10)
# print()
# print('---------------------------')
# print()
# Number(10, 42)


def Reverse(num: int = 1) -> int:
    i = 1
    while i <= num:
        print(f"{num-i}", end=" ")
        i += 1

Reverse(11)