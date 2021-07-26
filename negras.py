class Negras:
    def __init__(self,PosX , PosY):
        self.PosX=PosX
        self.PosY=PosY
        self.apparencia="n"
        self.MovimientoValido=False
        self.todoslosmovimiento=[(x,y)for x in range(25) for y in range(25)]
        self.EsRey=False

    def __str__(self):
        return self.apparencia
    def __eq__(self, other):
        return self.apparencia==other
    def setX(self,PosX):
        self.PosX=PosX
    def getX(self):
        return self.PosX
    def setY(self,Posy):
        self.PosY=Posy
    def getY(self):
        return self.PosY
    def get_movimientovalido(self,tablero):
        self.todoslosmovimiento.clear()
        self.tempX=self.PosX
        self.tempY=self.PosY
        self.movimentoValido=False
        self.PuedoSaltar=False
        if(self.espacioVacio(self.PosX+1,self.PosY+1,tablero)):
            self.movimientoValido=True
            self.todoslosmovimiento.append((self.PosX+1,self.PosY+1))
        if(self.espacioVacio(self.PosX+1,self.PosY-1,tablero)):
            self.movimentoValido=True
            self.todoslosmovimiento.append( (self.PosX+1,self.PosY-1) )

        if self.EsRey==True:
            if(self.espacioVacio(self.PosX-1,self.PosY+1,tablero)):
                    self.movimentoValido=True
                    self.todoslosmovimiento.append((self.PosX-1,self.PosY+1))
            if(self.espacioVacio(self.PosX-1 , self.PosY-1,tablero)):
                self.movimentoValido=True
                self.todoslosmovimiento.append((self.PosX-1,self.PosY-1))
    def movimiento(self,tablero,enemigo):
        self.puedosaltar=False
        if self.esunenemigo(self.tempX+1,self.tempY-1,tablero,enemigo):
            if self.espacioVacio(self.tempX+2,self.tempY-2,tablero):
                self.todoslosmovimiento.append((self.tempX+2,self.tempY-2))
                self.movimentoValido=True
                self.puedosaltar=True
                self.tempX+=2
                self.tempY-=2
                self.movimiento(tablero,enemigo)
        if self.esunenemigo(self.tempX+1,self.tempY+1,tablero,enemigo):
            if self.espacioVacio(self.tempX+2,self.tempY+2,tablero):
                self.todoslosmovimiento.append((self.tempX+2,self.tempY+2))
                self.movimentoValido=True
                self.puedosaltar=True
                self.tempY+=2
                self.tempY+=2
                self.movimiento(tablero,enemigo)
        if self.EsRey==True:
            if self.esunenemigo(self.tempX-1,self.tempY-1,tablero,enemigo):
                if self.espacioVacio(self.tempX-2,self.tempY-2,tablero):
                    self.todoslosmovimiento.append((self.tempX-2,self.tempY-2))
                    self.movimentoValido=True
                    self.puedosaltar=True
                    self.tempX-=2
                    self.tempY-=2
                    self.movimiento(tablero,enemigo)

            if self.esunenemigo(self.tempX-1,self.tempY+1,tablero,enemigo):
               if self.espacioVacio(self.tempX-2,self.tempY+2,tablero):
                        self.todoslosmovimiento.append((self.tempX-2,self.tempY+2))
                        self.movimentoValido=True
                        self.puedosaltar=True
                        self.tempX-=2
                        self.tempY+=2
                        self.movimiento(tablero,enemigo)


    def esunenemigo(self,posx,posy,tablero,enemigo):
        if posy <0 or posy>7 or posx<0 or posx>7:
            return False
        if isinstance(tablero[posx][posy],enemigo):
            return True
        return False
    def espacioVacio(self,posx,posy,tablero):
        if posy < 0 or posy >7 or posx<0 or posx>7:
            return False
        if tablero[posx][posy]==". ":
            return True
        return False
    def imprimirTodoslosMovimientos(self):
        contador=0
        for elem in self.todoslosmovimiento:
            print("{0}. {1}".format(contador,elem))
            contador+=1
    def chequeorey(self):
        print("Las negras es en un metodo de chequeo")
        print("{0}, {1}".format(self.PosX,self.PosY))
        if self.PosX==7:
            print("Pieza es Rey")
            print("{0}, {1}".format(self.PosX,self.PosY))
            self.EsRey=True
            self.apparencia="n"

    def movimientopieza(self,tablero,decision):
        if(self.movimentoValido==False):
            print('pieza negras {0}, {1} no tiene movimientos'.format(self.getX(),self.getY()) )
            return tablero
        else:
            coordenadas=self.todoslosmovimiento[decision]
            print('nueva coordenada={0},{1}'.format(coordenadas[0],coordenadas[1]))
            print('posicion Actual={0},{1}'.format(self.getX(),self.getY()))
            index=abs(self.PosX-coordenadas[0])
            print(index)
            for i in range(index):
                if coordenadas[1]>self.PosY:
                    tablero[self.PosX][self.PosY]= ". "
                    self.setX(self.PosX+1)
                    self.setY(self.PosY+1)
                    print('{0}, {1}'.format(self.getX(),self.getY()))
                else:
                    tablero[self.PosX][self.PosY]= ". "
                    self.setX(self.PosX+1)
                    self.setY(self.PosY-1)
                    print('{0},{1}'.format(self.getX(),self.getY()))
            self.setX(coordenadas[0])
            self.setY(coordenadas[1])
            tablero[self.getX()][self.getY()]=self
            self.todoslosmovimiento.clear()
        return tablero