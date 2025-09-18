vowelsList = ['a', 'e', 'i', 'o', 'u']
s = input("Enter input for vowel check : ")
s = s.replace(" ", "")
count = 0
for ch in s:
    if ch in vowelsList:
        print("vowel found : " + ch)
        count += 1
print("Total number of vowel found : " + str(count))
