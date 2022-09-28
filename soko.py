def crear_grilla(grilla):
        filas = len(grilla)
        for i in range(0,filas):
         grilla [i] =list(grilla[i])          
        return grilla 
     
def dimensiones(grilla) :
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla'''
    columnas = int(len(grilla[0]))
    filas = int(len(grilla))
    return columnas,filas

def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f)'''
    if grilla[f][c] == "#":
        return True

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f)'''
    if grilla[f][c] == "." or  grilla[f][c] =="+" or grilla[f][c] =="*" :
        return True

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f)'''
    if grilla[f][c] == "$" or grilla[f][c] =="*" :
        return True

def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f)'''
    if grilla[f][c] == "+" or grilla[f][c] == "@":
        return True 

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado'''
    c,f = dimensiones(grilla)
    for i in range(0,f):
        for z in range (0,c):
            if grilla[i][z] == "." or grilla[i][z] == "+":
               return False        
    return True


def mov (grilla,direccion,pos_x,pos_y):
         

        nueva_grilla =  crear_grilla(grilla[:])

        if direccion == (0,-1):
           pos_sigX_1 = pos_x
           pos_sigX_2 = pos_x
           pos_sigY_1 = pos_y-1
           pos_sigY_2 = pos_y-2

        if direccion == (0,1):
          pos_sigX_1 = pos_x
          pos_sigX_2 = pos_x
          pos_sigY_1 = pos_y+1
          pos_sigY_2 = pos_y+2

        if direccion == (1,0):
          pos_sigY_1 = pos_y
          pos_sigY_2 = pos_y
          pos_sigX_1 = pos_x+1
          pos_sigX_2 = pos_x+2

        if direccion == (-1,0):
          pos_sigY_1 = pos_y
          pos_sigY_2 = pos_y
          pos_sigX_1 = pos_x-1
          pos_sigX_2 = pos_x-2

        
        if nueva_grilla[pos_y][pos_x] =="@" and nueva_grilla[pos_sigY_1][pos_sigX_1] == " ":
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = " "
            print(nueva_grilla)
            nueva_grilla[pos_y][pos_sigX_1] = "@"
            return nueva_grilla
       
        elif nueva_grilla[pos_y][pos_x] == "@" and nueva_grilla[pos_sigY_1][pos_sigX_1] == "*" and hay_pared(nueva_grilla,pos_sigX_2,pos_sigY_2):
             return nueva_grilla 
        

        elif nueva_grilla[pos_y][pos_x] == "@" and hay_objetivo(nueva_grilla,pos_sigX_1,pos_sigY_1) and  nueva_grilla[pos_sigY_2][pos_sigX_2] == " " and  nueva_grilla[pos_sigY_2][pos_sigX_2] != ".":
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = " "
            nueva_grilla[pos_y][pos_sigX_1] = "+"
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == "@" and hay_caja(nueva_grilla,pos_sigX_1,pos_sigY_1)  and nueva_grilla[pos_sigY_2][pos_sigX_2] == " ":
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = " "
            nueva_grilla[pos_y][pos_sigX_1] = "@"
            nueva_grilla[pos_y][pos_sigX_2] = "$"
            return nueva_grilla
            

        elif nueva_grilla[pos_y][pos_x] == "@" and hay_caja(nueva_grilla,pos_sigX_1,pos_sigY_1)  and hay_objetivo(nueva_grilla,pos_sigX_2,pos_sigY_2) and  nueva_grilla[pos_sigY_2][pos_sigX_2] != "*" and  nueva_grilla[pos_sigY_1][pos_sigX_1] != "*":
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = " "
            nueva_grilla[pos_y][pos_sigX_1] = "@"
            nueva_grilla[pos_y][pos_sigX_2] = "*"
            return nueva_grilla

        elif nueva_grilla[pos_y][pos_x] == "+" and nueva_grilla[pos_sigY_1][pos_sigX_1] == " ":
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = "."
            nueva_grilla[pos_y][pos_sigX_1] = "@"
            return nueva_grilla
           
        elif nueva_grilla[pos_y][pos_x] == "+" and hay_objetivo(nueva_grilla,pos_sigX_1,pos_sigY_1):
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = "."
            nueva_grilla[pos_y][pos_sigX_1] = "+"
            return nueva_grilla
           
        elif nueva_grilla[pos_y][pos_x] ==  "+" and hay_caja(nueva_grilla,pos_sigX_1,pos_sigY_1) and nueva_grilla[pos_sigY_2][pos_sigX_2] == " ":
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = "."
            nueva_grilla[pos_y][pos_sigX_1] = "@"
            nueva_grilla[pos_y][pos_sigX_2] = "$"
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == "+" and hay_caja(nueva_grilla,pos_sigX_1,pos_sigY_1) and hay_objetivo(nueva_grilla,pos_sigX_2,pos_sigY_2):
            nueva_grilla[pos_y][pos_x] = "."
            nueva_grilla[pos_y][pos_sigX_1] = "@"
            nueva_grilla[pos_y][pos_sigX_2] = "*"
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == "+" and nueva_grilla[pos_sigY_1][pos_sigX_1] == "*" and nueva_grilla[pos_sigY_2][pos_sigX_2] == " ":
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = "."
            nueva_grilla[pos_y][pos_sigX_1] = "+"
            nueva_grilla[pos_y][pos_sigX_2] = "$"
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == "+" and nueva_grilla[pos_sigY_1][pos_sigX_1] == "*" and hay_objetivo(nueva_grilla,pos_sigX_2,pos_sigY_2):
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = "."
            nueva_grilla[pos_y][pos_sigX_1] = "+"
            nueva_grilla[pos_y][pos_sigX_2] = "*"
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == "@" and nueva_grilla[pos_sigY_1][pos_sigX_1] == "*" and nueva_grilla[pos_sigY_2][pos_sigX_2] == " ":
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = " "
            nueva_grilla[pos_y][pos_sigX_1] = "+"
            nueva_grilla[pos_y][pos_sigX_2] = "$"
            return nueva_grilla
            
        elif nueva_grilla[pos_y][pos_x] == "@" and nueva_grilla[pos_sigY_1][pos_sigX_1] == "*" and hay_objetivo(nueva_grilla,pos_sigX_2,pos_sigY_2):
            nueva_grilla[pos_y] = list(nueva_grilla[pos_y])
            nueva_grilla[pos_y][pos_x] = " "
            nueva_grilla[pos_y][pos_sigX_1] = "+"
            nueva_grilla[pos_y][pos_sigX_2] = "*"
            return nueva_grilla

        else:
            return nueva_grilla

def buscar_jugador (grilla):
    c,f = dimensiones(grilla)
    for i in range (0,f):
        for z in range (0,c):
            if grilla[i][z] == "@" or grilla[i][z] == "+":
                return z,i

def mover (grilla, direccion):
  c,f = buscar_jugador(grilla)
  grilla_2= mov(grilla,direccion,c,f)
  return grilla_2



