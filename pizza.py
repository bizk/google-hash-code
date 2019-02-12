# -*- coding: utf-8 -*-
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

print("Corroboramos")
print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[0][4])
print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3], matrix[1][4])
print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3], matrix[2][4])


        