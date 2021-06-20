import sys
file = open(sys.argv[1])
s = file.readline()
print(s)
t = file.readline()
print(t)
count = 0
for i in range(len(s)):
	if s[i] != t[i]:
		count += 1
print(count)