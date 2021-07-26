
from blancos import Blanco
from negras import Negras

class TablerodeJuego:
    def __init__(self):
        self.w, self.h=8,8
        self.listadenegra=[]
        self.listadeblanca=[]
        self.tablero=[[0 for x in range(self.w)]for y in range(self.h)]

    def espacioinilizacido(self):
        for i in range(self.w):
            for l in range(self.h):
                self.tablero[i][l] =". "
    def setPieza(self):
        contador=0
        for i in range(self.w):
            for l in range(self.w):
                if(i+l)%2 !=0 and  contador<24:
                    self.tablero[i][l]=Negras(i,l)
                    contador+=1
                elif(i+l)%2 !=0 and contador>39:
                    self.tablero[i][l]=Blanco(i,l)
                    contador+=1
                else:
                    contador+=1
    def movimiento(self,PosX,PosY,pieza,enemigo):
        if isinstance(self.tablero[PosX][PosY],pieza):
            print("pieza es {0}".format(pieza))
            inst=self.tablero[PosX][PosY]
            inst.get_movimientovalido(self.tablero)
            inst.movimiento(self.tablero,enemigo)
            inst.imprimirTodoslosMovimientos()

            if len(inst.todoslosmovimiento)==0:
                return False
            else:
                decisiones=int(input("Entra la opcion de tu movimiento"))
                self.tablero=inst.movimientopieza(self.tablero,decisiones)
                inst.chequeorey()
            return True
        else:
            inst=self.tablero[PosX][PosY]
            print(inst)
            print("not {0}".format(pieza))
            return False
    def chequeomovimientoValido(self,Posx,Posy,pieza,enemigo):
        if isinstance(self.tablero[Posx][Posy],pieza):
            inst=self.tablero[Posx][Posy]
            inst.get_movimientovalido(self.tablero)
            inst.movimiento(self.tablero,enemigo)
            if len(inst.todoslosmovimiento)==0:
                return False
            return True
    def ImprimirTablero(self):
        print("Imprimir Tablero")
        for i in range(self.w):
            for l in range(self.h):
                print(self.tablero[i][l],end= " ")
            print(end="\n")
    def UbicaciondeNegras(self):
        self.listadenegra.clear()
        for i in range(self.w):
            for l in range(self.h):
                if isinstance(self.tablero[i][l],Negras):
                    self.listadenegra.append((i,l))
    def UbicaciondeBlancas(self):
        self.listadeblanca.clear()
        for i in range(self.w):
            for l in range(self.h):
                if isinstance(self.tablero[i][l],Blanco):
                    self.listadeblanca.append((i,l))