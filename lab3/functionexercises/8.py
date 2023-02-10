list_input_size = int(input())
list_input = list()
for i in range(list_input_size):
    list_input.append(int(input()))

def spy_game(list_input: list):
    list_string = str()
    for i in list_input:
        list_string += str(i)
    if "007" in list_string:
        return True 
    else:
        return False 

print(spy_game(list_input))


