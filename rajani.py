l=input("Enter strings in list:").split( )
s=len(l[0])
s1=len(l[0])
for i in l:
    if s<len(i):
        s=len(i)
    if len(i)<s1:
        s1=len(i)
print("Largest length:",s)
print("Shortest length:",s1)
for i in l:
    k=len(i)
    if k==s:
        print("Large string:",i)
    if k==s1:
        print("short string:",i)

