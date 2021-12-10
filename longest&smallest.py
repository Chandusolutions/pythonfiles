l=["ram","srikar","bhavani"]
wordc=len(l)
eachword=len(l[0])
i=0
while i<len(l):
    if eachword<len(l[i]):
        eachword=len(l[i])
        i+=1

print(wordc)