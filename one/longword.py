
'''
Find the length of longest distinct value in given statement.
a="nithiyanayar"
output: nith
4'''
a = "abcdefghijka"
str= ""
for i in range(len(a)):
    if a[i] in str:
        break
    str+= a[i]
print(str)
print(len(str))
