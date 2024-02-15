original_list = [2,1.58,115,1.4552,4,.520,4,7440.1,42.04,112,.12]
only_int = [original_list[i] for i in range(len(original_list)) if type(original_list[i])==int]
only_float = [original_list[i] for i in range(len(original_list)) if type(original_list[i])==float]

print(f"{only_int = }")
print(f"{only_float = }")
