#https://www.geeksforgeeks.org/reverse-words-given-string-python/
str =" geeks quiz practice code"

s=str.split()[::-1] ##split is a builtin funtion that will put words of sentence in s and [::-1] is slicing that will reverse the s

l=[]
for i in s:
    l.append(i)

print(" ".join(l))

