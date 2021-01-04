from functions import run_r, run_w
def docpy():
    run_type = input(
        'Que Quieres Hacer ?(r = leer,w = escribir sin eliminar nada,a = eliminar todo y escribir): ')

    if run_type != 'r' and run_type != 'w' and run_type != 'a':
        return 'Ingrese argumentos validos'
    
    if run_type == 'r':
        return run_r()
    elif run_type == 'w':
        return run_w()

print(docpy())
