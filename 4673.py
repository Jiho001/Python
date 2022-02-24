a,b=set(range(1,10001)),set()
for i in range(1,10001): b.add(i + sum(map(int,list(str(i)))))
for i in sorted(a-b): print(i)