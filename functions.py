import os


def read(route, readAll, line=False):
    if verify_path(route, 'r'):
        file = open(route)
        if file.readable():
            if readAll:
                return file.read()
            else:
                line -= 1
                return file.readlines()[line]
        else:
            return 'La ruta de el archivo no es valida'
        file.close()
    else:
        return 'La ruta de el archivo no es valida'


def write(route, text, in_line=False, line=False):
    if verify_path(route):
        
        if in_line != True:
            file = open(route, 'a')
            if file.writable():
                file.write('\n' + text)
                return 'Hecho'
            file.close()
        elif in_line:
            content = open(route).read().splitlines()
            if line > len(content):
                return 'La linea no existe'
            
            line -= 1
            content[line] += text
            
            file = open(route, 'w')
            file.writelines('\n'.join(content))
            return 'Hecho'
            file.close()
    else:
        return 'La ruta de el archivo no es valida'


def verify_path(route):
    try:
        with open(route) as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False


def run_r():
    route = input('Ingresa la ruta de el archivo: ')
    readAll = input('Desea leer todo el archivo: ')

    if readAll.lower() == 'no':
        line = input('Ingrese el numero de la linea que desea leer: ')
        return read(route, False, int(line))
    elif readAll.lower() == 'si':
        return read(route, readAll)


def run_w():
    route = input('Ingresa la ruta de el archivo: ')
    text = input('Ingrese el texto: ')
    in_line = input('Desea Ingresar texto en una linea especifica ?: ')

    if in_line.lower() == 'si':
        line = input('En que linea desea hacerlo?: ')
        return write(route,text,True,int(line))
    elif in_line.lower() == 'no':
        return write(route,text)
