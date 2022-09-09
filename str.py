string = "manipal prolearn"
x=""
for i in string:
    if i=='A' or i=='a':
        x=x+'2'
    elif i=='E' or i=='e':
        x=x+'4'
    elif i=='I' or i=='i':
        x=x+'6'
    elif i=='O' or i=='o':
        x=x+'8'
    elif i=='U' or i=='u':
        x=x+'10'
    else:
        x=x+i


half=len(x)/2
print(half)
res=''
for i in range(len(x)):
    if i >= half:
        res += x[i].upper()
    else :
        res += x[i]

print(res)
