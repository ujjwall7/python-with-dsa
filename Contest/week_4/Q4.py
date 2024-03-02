"""
Q5. Ask a string from user. Replace all the space characters with “-”. Do not use replace() method.
"""

def replaceSpaces(sentence:str):
    new = sentence.split(" ")
    new_ = "-".join(i for i in new)
    return new_

print(replaceSpaces("my name is ujjwal sharma mai"))




