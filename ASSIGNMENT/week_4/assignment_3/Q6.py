"""
Q6. Write a python program to ask a string from user. Then count the
number of vowels and number of consonants in that string.
"""

def CountAlphabet(string:str):
    vowels_count = 0
    consonents_count = 0
    for i in string:
        if i == 'a' or i=='A' or i == 'e' or i=='E' or i == 'i' or i=='I' or i == 'o' or i=='O' or i == 'u' or i=='U':
            vowels_count += 1  
        else:
            consonents_count +=1
    
    return f"{vowels_count = } and {consonents_count = }"

print(CountAlphabet("Megha Sharma"))







