import math
import cmath

print("Нужно ввести комплексные коэффициенты?")
otv=input("Ваш ответ(Y/N) = ")

#complex
if otv =='Y':

    a = complex(input('введите коэффициент а: \n a='))
    b = complex(input('введите коэффициент b: \n b='))
    c = complex(input('введите коэффициент c: \n c='))
    print(a,'x^2+',b,'x+',c,' = 0', sep="")

    discr = b**2-4*a*c
    print('Дискриминант=', discr)

    
    print('x1=''-',b,'-',u'\u221a','(',discr,')','/',(2*a),sep='')
    print('x2=''-',b,'+',u'\u221a','(',discr,')','/',(2*a),sep='')

#float    
else:
    
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
    elif discr < 0:
        x1 = (-b+1j*math.sqrt(abs(discr)))/(2*a)
        x2 = (-b-1j*math.sqrt(abs(discr)))/(2*a)
        print('2 корня:\nx1 =', x1, 'x2 =', x2)