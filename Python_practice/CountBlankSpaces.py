while True:
    s = input("Enter a string for space count : ")
    res = 0
    for ch in s:
        if ch == ' ':
            res += 1
    print(res)
