def squares(N):
    for i in range(1, N+1):
        yield i*i
for square in squares(5):
    print(square)