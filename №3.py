import math

a = float(input('введите коэффициент а: \n a='))
b = float(input('введите коэффициент b: \n b='))
c = float(input('введите коэффициент c: \n c='))
print(a,'x^2+',b,'x+',c,' = 0', sep="")

discr = b**2-4*a*c
print('Дискриминант=', discr)

if discr > 0:
    x1 = (-b+math.sqrt(discr))/(2*a)
    x2 = (-b-math.sqrt(discr))/(2*a)
    print('2 корня:\nx1 =', x1, 'x2 =', x2)
elif discr == 0:
    x = (-b)/(2*a)
    print('1 корень:\nx =', x)
else:
    print('корней нет')

