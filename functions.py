import os
from colorama import Fore, Back, Style

# Lectura

def read(route, readAll, line=False):
    if verify_path(route):
        file = open(route,'r')
        if file.readable():
            if readAll:
                print(Fore.BLACK,file.read())
            else:
                line -= 1
                print(Fore.BLACK,file.readlines()[line])
        else:
            print(Fore.RED,'La ruta de el archivo no es valida')
        file.close()
    else:
        print(Fore.RED,'La ruta de el archivo no es valida')
    exit()

# Escritura

def write(route, text, in_line=False, line=False):
    if verify_path(route):

        if in_line != True:
            file = open(route, 'a')
            if file.writable():
                file.write('\n' + text)
                print('Hecho')
            file.close()
        elif in_line:
            content = open(route).read().splitlines()
            if line > len(content):
                print('La linea no existe')

            line -= 1
            content[line] += text

            file = open(route, 'w')
            file.writelines('\n'.join(content))
            print('Hecho')
            file.close()
    else:
        print(Fore.RED,'La ruta de el archivo no es valida')
    exit()

# Escritura y borrado


def delete_write(route, text):
    if verify_path(route):
        file = open(route, 'w')
        file.write(text)
        print('Hecho')
        file.close()
    else:
        print(Fore.RED,'La ruta de el archivo no es valida')
    exit()

# Creacion de archivos

def create_doc(route, name):
    if verify_dir(route):
        file = open(route + name,'w')
        file.write('Gracias por usar mi script')
        print('Hecho')
        file.close()
    else:
        print(Fore.RED,'La ruta de el archivo no es valida')
    exit()


# Verificacion de rutas

def verify_dir(route):
    if os.path.isdir(route):
        return True
    else:
        return False

def verify_path(route):
    try:
        with open(route) as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

# Correr la lectura


def run_r():
    route = input('Ingresa la ruta de el archivo: ')
    readAll = input('Desea leer todo el archivo: ')

    if readAll.lower() == 'no':
        line = input('Ingrese el numero de la linea que desea leer: ')
        print(Fore.BLACK,read(route, False, int(line)))
    elif readAll.lower() == 'si':
        print(read(route, readAll))

# Correr la escritura


def run_w():
    route = input('Ingresa la ruta de el archivo: ')
    text = input('Ingrese el texto: ')
    in_line = input('Desea Ingresar texto en una linea especifica ?: ')

    if in_line.lower() == 'si':
        line = input('En que linea desea hacerlo?: ')
        print(write(route, text, True, int(line)))
    elif in_line.lower() == 'no':
        print(write(route, text))

def run_a():
    route = input('Ingresa la ruta de el archivo: ')
    text = input('Ingrese el texto: ')
    print(delete_write(route,text))

def run_c():
    route = input('Ingresa la ruta de el archivo: ')
    name = input('Ingresa el nombre con la extencion de el archivo: ')
    print(create_doc(route,name))

