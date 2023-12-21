while True:
    dic = {'tiempo' : 'km'} 
    corredor = input('Introduzca su nombre: ')
    tiempo = input('Introduzca la hora: ')
    kilometro = input('Introduzca el kilometraje en el que se encuentra: ')
    t = input('¿Ha terminado la carrera? ')
    if t == 'si':
        print( corredor.title() , 'a las', tiempo , 'estaba en el km', kilometro )
        break
    






