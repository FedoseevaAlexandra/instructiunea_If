a=int(input('prima nota '))
b=int(input('a doua nota '))
c=int(input('a treia nota '))
if (a>10) or (b>10) or (c>10):
    print ('In Moldova nota cea mai mare e 10)')
else:
    if c>=8:
      print(a, b, c)
    else:
        print(max(a,b))
