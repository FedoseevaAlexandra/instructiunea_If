xa=int(input('nr bile albe mici '))
xr=int(input('nr bile rosii mici '))
xv=int(input('nr bile verzi mici '))
ya=int(input('nr bile albe mari '))
yr=int(input('nr bile rosii mari '))
yv=int(input('nr bile verzi mari '))
xt=xa+xr+xv
yt=ya+yr+yv
print('total ', xt+yt, 'bile')
if xt>yt:
    print('bile mici sunt mai multe (',xt,')')
elif xt==yt:
    print('egale')
else:
    print('bile mari sunt mai multe (', yt,')')
a=xa+ya
r=xr+yr
v=xv+yv
if ((a>r) and (a>v))or((a>r) and (r==v)):
    print('albe sunt mai multe', a)
if ((v>r) and (a<v))or((v>r) and(r==a)):
    print('verzi sunt mai multe', v)
if ((a<r) and (r>v))or((r>v) and(v==a)):
    print('rosii sunt mai multe', r)
if ((a==r) and (a>v)):
    print('albe si rosii sunt mai multe', a)
if (a>r) and (a==v):
    print('albe  si verzi sunt mai multe', a)
if (v==r) and (a<v):
    print('verzi si rosii sunt mai multe', v)


