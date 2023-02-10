def ThatIsPrime(number: int):
    if number == 0 or number == 1:
        return False
    boolka = True
    for i in range(2, number):
        if(number % 2 == 0):
            boolka = False 
    if(boolka):
        return True 
    else:
        return False 
    

def filter_prime(all_numbers: list):
    prime_numbers = list()
    for i in all_numbers:
        if(ThatIsPrime(i)):
            prime_numbers.append(i)
    return prime_numbers


size_list = int(input())
list_1 = list()

for i in range(size_list):
    list_1.append(int(input()))

print(filter_prime(list_1))

