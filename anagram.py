def anagram(s):
    slist = []
    for ch in s.lower():
        slist.append(ch)

    sdict = {}
    for ch in slist:
        if ch not in sdict:
            sdict[ch] = 1
        else:
            sdict[ch] = sdict[ch] + 1

    return sdict

s1 = str(input("Enter the first string:"))
s2 = str(input("Enter the second string:"))

a = anagram(s1)
b = anagram(s2)

if a == b:
    print (s1, "and", s2, "are Anagram")
else:
    print("Not Anagram")
