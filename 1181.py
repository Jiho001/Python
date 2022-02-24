words=set()
for i in range(int(input())):
    words.add(input())
words=list(words)
words.sort(key=lambda x:((len(x),x)))
for i in words:
    print(i)