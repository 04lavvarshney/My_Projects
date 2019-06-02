def ly(a):
    x=366
    y=365
    if a%100==0:
        if a%400==0:
            return x
        else:
            return y
    else:
        if a%4==0:
            return x
        else:
            return y

d,m,y=map(int,input("enter the date in the format dd/mm/yyyy: ").split("/"))
#print(d)
#print(m)
#print(y)
a=ly(y)
#print(a)

if a==366:
    l=[31,29,31,30,31,30,31,31,30,31,30,31]
    s=0
    for i in range(m-1):
        s+=l[i]
    s=s+d
    #print(s)
    f=a-s
    print("days left=",f)
elif a==365:
    l=[31,28,31,30,31,30,31,31,30,31,30,31]
    s=0
    for i in range(m-1):
        s+=l[i]
    s=s+d
    #print(s)
    f=a-s
    print("days left=",f)


