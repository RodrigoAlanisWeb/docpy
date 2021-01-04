from functions import run_r, run_w, run_a, run_c

# Funcion principal

def docpy():
    run_type = input(
        'Que Quieres Hacer ?(r = leer,w = escribir sin eliminar nada,a = eliminar todo y escribir,c = crear archivo): ')

    if run_type != 'r' and run_type != 'w' and run_type != 'a' and run_type != 'c':
        return 'Ingrese argumentos validos'

    if run_type == 'r':
        return run_r()
    elif run_type == 'w':
        return run_w()
    elif run_type == 'a':
        return run_a()
    elif run_type == 'c':
        return run_c()


# Ejecutar el programa
if __name__ == "__main__":
    docpy()
