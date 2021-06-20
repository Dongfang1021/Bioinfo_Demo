import sys
file = sys.argv[1]
file = open(file, 'r')
s = file.readline().strip()
print(s)
print("*"*100)
t = file.readline().strip()
print(t)
l = len(t)
print(l)
list = []
for i in range(len(s)-l):
	if s[i:(i+l)] == t:
		list.append(i + 1)
print(*list)