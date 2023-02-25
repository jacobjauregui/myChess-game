# def test_var_args(first_arg, *argv):
#     print("Argumento posisional: ", first_arg)
#     for arg in argv:
#         print("otros argumentos :", arg)

# test_var_args('1er argumento','2do arg','3er arg','4to arg')

# def test_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))


def asincronismo(fn, args, *, callback):
    '''
    Ejecuta una función de forma asíncrona.
    fn: Función principal
    args: Argumentos de la función principal
    callback: Función que se ejecutará al finalizar la función principal
    '''
    result = fn(*args)
    callback(result)
    

def call_back(result):
    print(f'El resultado es: {result}')


def fun(a, b):
    return a*b + b*a



asincronismo(fun, (2, 4), callback=call_back)