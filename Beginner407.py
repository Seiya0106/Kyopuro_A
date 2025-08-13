A, B = map(int, input().split())

div = A / B
div_t = A // B
if div - div_t >= (div_t + 1) - div:
    print(div_t + 1)
else:
    print(div_t)
