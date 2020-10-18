ac=input("anul curent ") 
lc=input("luna curenta ") 
zc=input("ziua curenta ")
an=input('anul nasterii ') 
ln=input('luna nasterii ') 
zn=input('ziua nasterii ')
if (ln>lc)and(zn>zc):
    print((ac-an)+1,' ani')
else:
    print((ac-an),' ani')
