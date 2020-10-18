x=int(input('locul '))
if x>100:
    print('nu va primi')
else:
    if x%4==1:
        print('alba')
    if x%4==2:
        print('rosie')
    if x%4==3:
        print('albastra')
    if x%4==0:
        print('neagra')