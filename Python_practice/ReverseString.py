while True:
    s = input("Enter input :")
    s = s.replace(" ", "")
    res = ''
    for ch in s:
        res = ch + res
    print(res)
