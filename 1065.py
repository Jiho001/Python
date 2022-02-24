n = int(input())
cnt=0
if n<100: print(n)
else:
    for i in range(100,n+1):
        if (i//100-i//10%10) == (i//10%10-i%10):
            cnt += 1
    print(cnt+99)