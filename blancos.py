class Blanco:
    def __init__(self,posX,posy):
        self.posX=posX
        self.posy=posy
        self.aparencia="b "
        self.movimientoValido=False
        self.todoslosmovimiento=[(x, y)for x in range(25)for y in range(25)]
        self.EsRey=False
        self.abajo_derecha=True
        self.abajo_izquierdo=True
        self.arriba_derecha=True
        self.arriba_izquierda=True
        self.movimientoarriba=False
        self.movimientoabajo=False

    def __str__(self):
        return self.aparencia
    def __eq__(self, other):
        return self.aparencia==other
    def setX(self,posx):
        self.posX=posx
    def getX(self):
        return self.posX
    def setY(self,posy):
        self.posy=posy
    def getY(self):
        return self.posy
    def get_movimientovalido(self,tablero):
        self.todoslosmovimiento.clear()
        self.tempx=self.posX
        self.tempy=self.posy
        self.movimientoValido=True
        self.Arriba_derecha=True
        self.Arriba_izquierda=True
        self.abajo_derecha=True
        self.abajo_izquierdo=True
        if(self.espacioVacio(self.posX-1,self.posy+1,tablero)):
            self.movimientoValido=True
            self.todoslosmovimiento.append((self.posX-1,self.posy+1))
        if(self.espacioVacio(self.posX-1 ,self.posy-1,tablero)):
            self.movimientoValido=True
            self.todoslosmovimiento.append((self.posX-1,self.posy -1 ))
        if self.EsRey==True:
            if (self.espacioVacio(self.posX+1,self.posy+1,tablero)):
                self.movimientoValido=True
                self.todoslosmovimiento.append((self.posX+1,self.posy-1))
            if(self.espacioVacio(self.posX+1,self.posy-1,tablero)):
                self.movimientoValido=True
                self.todoslosmovimiento.append((self.posX+1,self.posy-1))
            if(self.espacioVacio(self.posX+1,self.posy-1,tablero)):
                self.movimientoValido=True
                self.todoslosmovimiento.append((self.posX+1,self.posy-1))
    def movimiento(self,tablero,enemigo):
        self.saltar=False
        if self.arriba_derecha == True and self.Esuneenemigo(self.tempx - 1, self.tempy - 1, tablero, enemigo):
            if self.espacioVacio(self.tempx - 2, self.tempy -2, tablero):
                self.todoslosmovimiento.append((self.tempx - 2, self.tempy - 2))
                self.movimientoValido = True
                self.saltar = True
                self.tempx += 2
                self.tempy += 2
                self.abajo_derecha = False
                self.abajo_izquierdo = True
                self.arriba_derecha = True
                self.arriba_izquierda = True
                self.movimiento(tablero, enemigo)

        if self.arriba_izquierda==True and self.Esuneenemigo(self.tempx-1,self.tempy+1,tablero,enemigo):
            if self.espacioVacio(self.tempx-2,self.tempy+2,tablero):
                self.todoslosmovimiento.append((self.tempx-2,self.tempy+2))
                self.movimientoValido=True
                self.saltar=True
                self.tempx-=2
                self.tempy-=2
                self.abajo_izquierdo=False
                self.abajo_derecha=True
                self.arriba_derecha=True
                self.arriba_izquierda=True
                self.movimiento(tablero,enemigo)

        if self.abajo_izquierdo==True and self.EsRey==True:
            if self.Esuneenemigo(self.tempx+1,self.tempy-1,tablero,enemigo):
                if self.espacioVacio(self.tempx+2,self.tempy-2,tablero):
                    self.todoslosmovimiento.append((self.tempx+2,self.tempy-2))
                    self.movimientoValido=True
                    self.saltar=True
                    self.tempx+=2
                    self.tempy-=2
                    self.arriba_derecha=False
                    self.abajo_derecha=True
                    self.abajo_izquierdo=True
                    self.arriba_izquierda=True
                    self.movimiento(tablero,enemigo)
            if self.abajo_derecha==True and self.Esuneenemigo(self.tempx+1,self.tempy+1,tablero,enemigo):
                if self.espacioVacio(self.tempx+2,self.tempy+2,tablero):
                    self.todoslosmovimiento.append((self.tempx+2,self.tempy+2))
                    self.movimientoValido=True
                    self.saltar=True
                    self.tempx-=2
                    self.tempy+=2
                    self.arriba_izquierda=False
                    self.abajo_derecha=True
                    self.arriba_derecha=True
                    self.arriba_derecha=True
                    self.movimiento(tablero,enemigo)


    def Esuneenemigo(self,posX,posY,tablero,enemigo):
        if posY < 0 or posY>7 or posX<0 or posX>7:
            return  False

        if isinstance(tablero[posX][posY],enemigo):
            return True
        return False
    def espacioVacio(self,PosX,PosY,tablero):
        if PosY <0 or PosY>7 or PosX<0 or PosX>7:
            return False
        if tablero[PosX][PosY]== ". ":
            return True
        return False
    def imprimirTodoslosMovimientos(self):
        contador=0
        for  elementos in self.todoslosmovimiento:
            print("{0}. {1}".format(contador,elementos))
            contador+=1
    def chequeorey(self):
        if self.posX==0:
            self.EsRey=True
            self.aparencia="bK"
    def movimientopieza(self,tablero,decisiones):
        if self.movimientoValido==False:
            print('Blanco pieza {0} , {1} no tiene movimientos'.format(self.getX(),self.getY()))
            return tablero
        else:
            coordenadas=self.todoslosmovimiento[decisiones]
            index=abs(self.posX-coordenadas[0])
            if(self.posX>coordenadas[0]):
                self.movimientoarriba=True
            if(self.posX<coordenadas[0]):
                self.movimientoabajo=True
            for i in range(index):
                tablero[self.posX][self.posy]= ". "
                print("coordenasmovimiento={0} posicionActual={1}".format(coordenadas[1],self.posy))
                if self.movimientoarriba==True:
                    if coordenadas[1]>self.posy:
                        print("coordenamovimiento={0} posicionActual={1}".format(coordenadas[1], self.posy))
                        print("moviendo derecha y Arriba")
                        self.setX(self.posX-1)
                        self.setY(self.posy+1)
                    else:
                        print("coordenasmovimiento={0} posicionActual={1}".format(coordenadas[1], self.posy))
                        print("Movimiento arriba y abajo")
                        self.setX(self.posX-1)
                        self.setY(self.posy-1)
                if self.movimientoabajo==True:
                    for i in range(index):
                        if coordenadas[1]>self.posy:
                            tablero[self.posX][self.posy]=". "
                            self.setX(self.posX+1)
                            self.setY(self.posy+1)
                            print('{0}, {1}'.format(self.getX(),self.getY()))
                        else:
                            tablero[self.posX][self.posy]=". "
                            self.setX(self.posX+1)
                            self.setY(self.posy-1)
                            print('{0}, {1}'.format(self.getX(),self.getY()))
            print('{0}, {1}'.format(self.getX(), self.getY()))
        print(list)
        self.setX(coordenadas[0])
        self.setY(coordenadas[1])
        tablero[self.getX()][self.getY()]=self
        self.todoslosmovimiento.clear()
        return tablero