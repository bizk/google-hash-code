    # -*- coding: utf-8 -*-

#
#       T E S T 
#
tom = 0 #Tomatoes
mus = 0 #Mushroom
global matrix
global h
global l

#We create the balance function that allow us to calculate the ifference betwen tomatoes and mushrooms to know if the we are dividing propertly
class Cor:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def calculateBalance(t1, m1): 
    if t1 >= m1:
        balance = t1/m1
    else:
        balance = m1/t1
    return balance

def updateBalance(t1,m1):
    tom =- t1
    mus =- m1
    return(calculateBalance(tom, mus), tom, mus)
    
#Calcula si tenemos la proporcion correcta de tomates y cosas
def calculateBalanceOverSlice(r1, r2, c1,c2): #r1 and c1 are the start and r2 and c2 are the end of the slice, this function is to calculate if the balance of a slice is viable
    totalRows = r2 - r1
    totalColumns = c2-c1
    tom = 0
    mus = 0
    for x in totalRows:
        for y in totalColumns:
            if matrix[x+r1][y+c1]== "T":
                tom += 1
            elif matrix[x+r1][y+c1] == "M":
                mus += 1
    return calculateBalance(tom, mus)

        
#
# F I L E - R E A D I N G
#
with open("a_example.in") as f: #We open the file
    info = f.readline() #We get the first line of the file and get the information
    row = int(info[0])
    column = int(info[2])
    l = int(info[4])
    h = int(info[6])
    print("Rows:", row, " Columns:", column,"Min:", l, "Max:",h)    
    
    matrix = [[0 for x in range(column)] for y in range(row)] #We initialize the 2d array...
    i = 0
    j = 0
    while True: #While we are still in the file
        character = f.read(1)#We read 1 character
        if not character: #we reach the end of the file
            break
        else:
            if character == "\n":
                i += 1
                j = 0
            else:
                matrix[i][j] = character
                j += 1
                if character == "T":
                    tom += 1
                elif character == "M":
                    mus += 1

f.close()

balance = calculateBalance(tom, mus)
print("Hongos:",mus,"Tomates:",tom,"Balance", balance)

print("Corroboramos...")
print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[0][4])
print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3], matrix[1][4])
print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3], matrix[2][4])


#
#
#
print("Filas:",len(matrix),"Columnas:",len(matrix[0]))

size = len(matrix)*len(matrix[0])
#balance = calculateBalanceOverSlice(r1,r2,c1,c2)

class pieza:
    def __init__(self, r1,r2,c1,c2, padre):
        self.r1 = r1 #r1 = start row from original matrix, r2 end row from original mtri
        self.r2 = r2 
        self.c1 = c1 #Same from rows for columns
        self.c2 = c2
        self.padre = padre #Objeto pieza
        self.hijos = []
        
    def updateHijos(self, hijos):
        self.hijos = hijos
        
    #La idea de esta funciones, por un lado encontrar un cuadrado que cumpla las cndiciones y x otro lado que chequee que los que queden tambien lo sean
    #Chequeear los otros puede entrar en otra funcion, para eso esta el tema de hijos
    def rotarYReformar():
        balancePieza = calculateBalanceOverSlice(self.r1, self.r2, self.c1, self.c2)
        row = r2-r1
        column = c2-c1
        #Tenemos que ver como darle forma y reforma a las piezas
        while row*column <= h*2 or balancePieza != 1:
            
            
        #Si pasa este limite y no la encontro, nose puede y debemos volver al padre y retroceder
        

#Esta funcion nos sirve para controlar si la ppieza es indivisiblle o no cumple las condiciones, es util o puede ser cortada
def chequearSlice(r1,r2,c1,c2, h, l):
    maxBalance = h/l
    balanceSlice = calculateBalanceOverSlice(r1,r2,c1, c2)
    if balanceSlice > maxBalance or balanceSlice == 0: #Si NO VA A EXISTIR DIVISION QUE LE VENGA BIEN
        return -1
    else:
        if (r2-r1)*(c2-c1) <= h*2: #So Podemos dividirla 
            return 0
        else:
            return 1 #Si cumple con la minima
      
        
    



