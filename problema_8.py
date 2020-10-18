a=int(input('nr1 '))
b=int(input('nr2 '))
if(a%2==0)and(b%2==0):
    print(max(a,b))
if(a%2==0)and(b%2!=0):
    print(a)
if(a%2!=0)and(b%2==0):
    print(b)
if(a%2!=0)and(b%2!=0):
    print('nu exista nr par')


