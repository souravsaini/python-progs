s = "SOURAV"
list=[]
for i in range(0,len(s)):
	list.append(ord(s[i]))

str1=int(''.join(map(str, list)))
print(str1)