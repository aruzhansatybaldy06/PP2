s=input()
upper=0
lower=0
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        lower+=1
    else:
        upper+=1
print(upper, lower)