s = "abc"
print(len(s))
t = "ahbgdc"
i = 0

for j in range(len(s)):
    print(j)
    if s[j] != t[i]:
        i += 1

print(i)