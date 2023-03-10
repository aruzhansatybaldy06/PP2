s = str(input())
def pal(s) :
    ss = s[::-1]
    if ss==s:
        print('Given string is a palindrome')
    else: 
        print('Given string is not a palindrome')
pal(s)