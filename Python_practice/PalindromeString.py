while True:
    s = input("Enter a string here :")
    s = s.replace(" ", "")
    rev = ''
    for c in s:
        rev = c + rev
    if rev == s:
        print("Yes it is palindrome")
    else:
        print("NO it is not palindrome")
