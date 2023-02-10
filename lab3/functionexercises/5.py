from itertools import permutations

string_input = str(input())

def permut_of_str(string: str):
    string = list(permutations(string))
    list_1 = []
    for i in string:
        k = str()
        for s in i:
            k+=s 
        list_1.append(k)

    return list_1

print(*permut_of_str(string_input))
