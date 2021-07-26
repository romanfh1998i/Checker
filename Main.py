from Tablero import TablerodeJuego
from blancos import Blanco
from negras import Negras

Tablero=TablerodeJuego()
print("Bienvenido al Juego de damas")
print("============================")
Tablero.espacioinilizacido()
Tablero.setPieza()
Tablero.ImprimirTablero()

MovimientodeNegroValido=[]
MovimientodeBlancosValido=[]
contador=0
VictoriaDeblanco=0
VictoriaDeNegros=0


while True:
    Tablero.ImprimirTablero()
    movimientoPermitido=False
    MovimientodeBlancosValido.clear()
    Tablero.UbicaciondeBlancas()
    for i in range(len(Tablero.listadeblanca)):
        coordenas=Tablero.listadeblanca[i]
        if Tablero.chequeomovimientoValido(coordenas[0],coordenas[1],Blanco,Negras):
            MovimientodeBlancosValido.append(coordenas)

    if len(MovimientodeBlancosValido)==0:
        print("Jugador 2 Ganas")
        VictoriaDeblanco += 1
        numerodepartida="Partidas ganadas"
        print(VictoriaDeblanco)
        print(numerodepartida)
        break

    while(movimientoPermitido==False):
        print("Turno de Jugador 1")
        print("Aqui estan Movimientos Validos")
        print(MovimientodeBlancosValido)
        decisiones=int(input("Entra la opcion correspondiente a la lista indicada de tu index"))
        movimiento=MovimientodeBlancosValido[0]
        coordenas=Tablero.listadeblanca[decisiones]
        print("Movimiento {0}".format(movimiento))
        movimientoPermitido=Tablero.movimiento(coordenas[0],coordenas[1],Blanco,Negras)
        Tablero.ImprimirTablero()
    movimientoPermitido=False
    Tablero.UbicaciondeNegras()
    MovimientodeNegroValido.clear()
    for i in range(len(Tablero.listadenegra)):
        coordenas=Tablero.listadenegra[i]
        if Tablero.chequeomovimientoValido(coordenas[0],coordenas[1],Negras,Blanco):
            MovimientodeNegroValido.append(coordenas)
    if len(MovimientodeNegroValido)==0:
        print("Jugador 1 gana")
        VictoriaDeNegros += 1
        numerodepartida = "Partidas ganadas"
        print(VictoriaDeNegros)
        print(numerodepartida)
        break

    while(movimientoPermitido==False):
        print("Jugador 2 turno")
        print("Aqui estan tus movimientos validos")
        print(MovimientodeNegroValido)
        decisiones=int(input("Entra la opcion correspondiente a la lista indicada de tu index"))
        movimiento=MovimientodeNegroValido[decisiones]

        print("Movimientos {0}".format(movimiento))
        movimientoPermitido=Tablero.movimiento(coordenas[0],coordenas[1],Negras,Blanco)
