#https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/

str="GeeksforGeeks"
pos=2
a=str[:pos]+str[pos+1:]
print(a)