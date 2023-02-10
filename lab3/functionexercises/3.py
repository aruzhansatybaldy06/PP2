def solve(numheads, numlegs):
    x = ((2 * numheads) - numlegs ) / - 2
    y = numheads - x
    return int(x), int(y)
print(solve(35, 94))

