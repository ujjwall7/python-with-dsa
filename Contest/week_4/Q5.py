"""
Q4. Ask a sentence from user. Then ask a integer k from user. Print all the words which are greater or equal to k.
"""



def k(sentence:str, index_:int):
    new = sentence.split(' ')
    _new = " ".join(new[i] for i in range(1, index_+1))
    print(_new)
x = input("Enter the sentence = ")
_x = int(input("Enter the word in int = "))
k(x, _x)











