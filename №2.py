x,y=0,0
while True:
    print('текущие координаты:', x, y)
    step = input('укажите направление движения (влево, вправо, вверх или вниз):\nдля выхода введите команду стоп.\n')
    if step == 'стоп':
        break
    a = int(input('укажите количество шагов:'))
    if a < 0:
        print ('отрицательные шаги недопустимы')
    elif step == 'вправо':
        x+=a
    elif step == 'влево':
        x-=a
    elif step == 'вниз':
        y-=a
    elif step == 'вверх':
        y+=a
    print('текущие координаты:', x, y)