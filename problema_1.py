n1=int(input('dati nr elevului'))
n2=int(input('dati nr elevului'))
n3=int(input('dati nr elevului'))
p1=input('dati punctajul elevului 1')
p2=input('dati punctajul elevului 2')
p3=input('dati punctajul elevului 3')
if (p1>p2) and (p1>p3):
    print('punctaj maxim are elevul nr',n1)
if (p2>p1) and (p2>p3):
    print('punctaj maxim are elevul nr',n2)
if (p3>p2) and (p3>p31): 
    print('punctaj maxim are elevul nr',n3)  
if (p1==p2) and (p1>p3) and (p2>p3):
    print(n1,n2,'au acelas punctaj')
if (p2==p3) and (p2>p1) and (p3>p1):
    print(n2,n3,'au acelas punctaj')
if (p1==p3) and (p2<p1) and (p3>p2):
    print(n1,n3,'au acelas punctaj')
else:
    print('toti au acelas punctaj')
