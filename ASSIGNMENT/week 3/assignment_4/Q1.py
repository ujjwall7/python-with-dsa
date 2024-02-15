"""
Q1. Make a list of your own. Make two more empty list like odd and even. 
Put all the even numbers from original list to even and odd numbers to 
odd and print both lists. (Don’t remove anything from original one).
"""


def listQuestion(original_list: list[int]):
    even = []
    odd = []
    for x in range(len(original_list)):
        if original_list[x] % 2 == 0:
            even.append(original_list[x])
        else:
            odd.append(original_list[x])
    return f"even: {even}", f"odd: {odd}"


print(
    listQuestion(
        original_list=[
            1,
            2,
            3,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
        ]
    )
)
