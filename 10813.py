n = int(input())
p = []
for _ in range(n):
    a, b = input().split()
    a = int(a)
    p.append([a, b])

p.sort(key = lambda x:x[0]) #key = 나이로 고정

for i in p:
    print(i[0],i[1])


