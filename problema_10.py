g=int(input('nr de gaini '))
b=int(input('nr boabe '))
c=b%g
gb=b//g
if c>gb:
    print('Clapon a primit cu',c-gb,' boabe mai mult')
if c==gb:
    print('egalitate ',c)
else:
    print('gainile au primit cu',gb-c,' boabe mai mult')
