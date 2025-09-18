k = 0
for i in range(1, 8):
    k += 1 if i <= 4 else -1
    for j in range(1, 8):
        if 5 - k <= j <= 3 + k:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
