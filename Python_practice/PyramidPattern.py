for i in range(5):
    for j in range(8):
        if 5 - i <= j <= 3 + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
