import random

# Definimos el mapa de la casa
casa = {
    'sala': {
        'descripcion': 'Estás en la sala. Hay puertas al norte y al este.',
        'norte': 'cocina',
        'este': 'comedor',
        'objetos': [],
        'monstruo': False
    },
    'cocina': {
        'descripcion': 'Estás en la cocina. Hay una puerta al sur.',
        'sur': 'sala',
        'objetos': ['llave'],
        'monstruo': False
    },
    'comedor': {
        'descripcion': 'Estás en el comedor. Hay puertas al oeste y al norte.',
        'oeste': 'sala',
        'norte': 'dormitorio',
        'objetos': [],
        'monstruo': True
    },
    'dormitorio': {
        'descripcion': 'Estás en el dormitorio. Hay una puerta al sur.',
        'sur': 'comedor',
        'objetos': ['espada'],
        'monstruo': False
    }
}

# Estado inicial del jugador
jugador = {
    'ubicacion': 'sala',
    'inventario': [],
    'vida': 100
}

# Función para mover al jugador
def mover(direccion):
    ubicacion_actual = jugador['ubicacion']
    if direccion in casa[ubicacion_actual]:
        nueva_ubicacion = casa[ubicacion_actual][direccion]
        jugador['ubicacion'] = nueva_ubicacion
        print(f'Te has movido a {nueva_ubicacion}.')
        if casa[nueva_ubicacion]['monstruo']:
            print('¡Oh no! Hay un monstruo aquí.')
            jugador['vida'] -= 50
            if jugador['vida'] <= 0:
                print('¡Has sido derrotado por el monstruo!')
                exit()
    else:
        print('No puedes ir en esa dirección.')

# Función para tomar objetos
def tomar(objeto):
    ubicacion_actual = jugador['ubicacion']
    if objeto in casa[ubicacion_actual]['objetos']:
        casa[ubicacion_actual]['objetos'].remove(objeto)
        jugador['inventario'].append(objeto)
        print(f'Has tomado {objeto}.')
    else:
        print(f'{objeto} no está aquí.')

# Función principal del juego
def jugar():
    print('Bienvenido al juego de laberintos RPG.')
    print('Tu objetivo es recoger objetos y escapar de la casa, evitando a los monstruos.')
    print('Escribe "ir" seguido de una dirección (norte, este, sur, oeste) para moverte.')
    print('Escribe "tomar" seguido del nombre de un objeto para recogerlo.')
    print('Escribe "salir" para terminar el juego.')

    while True:
        ubicacion_actual = jugador['ubicacion']
        print(casa[ubicacion_actual]['descripcion'])
        if casa[ubicacion_actual]['objetos']:
            print('Objetos aquí:', ', '.join(casa[ubicacion_actual]['objetos']))
        if casa[ubicacion_actual]['monstruo']:
            print('¡Cuidado! Hay un monstruo aquí.')

        comando = input('> ').lower().split()

        if not comando:
            continue

        if comando[0] == 'ir':
            if len(comando) > 1:
                mover(comando[1])
            else:
                print('Especifica una dirección.')

        elif comando[0] == 'tomar':
            if len(comando) > 1:
                tomar(comando[1])
            else:
                print('Especifica un objeto.')

        elif comando[0] == 'salir':
            print('Gracias por jugar. ¡Hasta la próxima!')
            break

        else:
            print('Comando no reconocido.')

# Iniciar el juego
jugar()