def div(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in div(50):
    print(num)