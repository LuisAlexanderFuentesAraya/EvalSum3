import os
import time
import csv
from random import *

local={}
locales=['1) San bernardo   ','2) Calera de tango   ','3) Buin  ']


def limpiar():
    os.system('cls')



with open('archivoprueba.csv','w',newline='') as archivoprueba_csv:
    contenido=csv.writer(archivoprueba_csv)

def guardar(cliente,archivoprueba_csv):
    with open('archivoprueba.csv','a',newline='') as archivoprueba_csv:
        contenido=csv.writer(archivoprueba_csv)
        contenido.writerow(['Nro. Ped.','Cliente','Direccion','Sector','Saco 5KG','Saco 10KG','Saco 20KG'])
        contenido.writerow(cliente)
        
        
pedidos = []




def deseasseguir():
    acceso=1
    while acceso==1:
        try:
            sigues=int(input('''
                              Desea volver al menu ?
                             1) Si
                             2) No '''))
        except ValueError:
            print(' opcion equivocada')
        if sigues==1:
            menuprincipal()
        elif sigues==2:
            print(' Muchas gracias, espero verlo pronto')
            quit()
        else:
            print('opcion equivocada, reintente nuevamente')


def listarpedidos():
    print(' IMPRIENDO PEDIDOS....')
    time.sleep(2)
    with open('archivoprueba.csv','r') as archivoprueba_csv:
        contenido=csv.reader(archivoprueba_csv)
        for fila in contenido:
            print(fila)




def elmenu():
    print('''   CATPREMIUM --> REPARTO DE COMIDA DE GATO A DOMICILIO
                                            SACOS DE 5,10,20 KILOS
        1. Registrar pedido
        2. Listar todos los pedidos 
        3. Imprimir hoja de ruta 
        4. Salir del programa
                        ''')
    
def imprimirhojaderuta():
    print()
    print(locales)
    print()
    time.sleep(0.7)
    cuallocal=int(input(' selecciona el local donde se haran todos estos pedidos '))
    limpiar()
    datos = f''' LOCAL DONDE SE HARAN LOS PEDIDOS:  {cuallocal}  
                 PEDIDOS: 'Nro. Ped.','Cliente','Direccion','Sector','Saco 5KG','Saco 10KG','Saco 20KG'
                          {pedidos}'''
    with open('archivo1.txt','w') as archivo1_txt:
        archivo1_txt.write(datos)
        print(datos)






    
        
    




def registrarpedido():
    print(' FORMULANDO PEDIDO ')
    num=randint(1,1000)
    nombre=input(' Escribe tu nombre completo:    ')
    direccion=input(' Escribe tu direccion (NOMBRE Y NUMERO) :          ')
    sector=input(' escribe tu comuna :      ')
    print()
    print(''' PORFAVOR INGRESA EL NUMERO DE SACOS QUE LLEVARAS
               ''')
    print(''' EJEMPLO 
              5 kilos -> x
              10 kilos -> x
              20 kilos -> x     ''')
    print(' AHORA TU : ')
    print()
    kilos5=int(input( ' 5 kilos --> '))
    kilos10=int(input( ' 10 kilos --> '))
    kilos20=int(input( ' 20 kilos --> '))
    cliente=(num,nombre,direccion,sector,kilos5,kilos10,kilos20)
    archivoprueba_csv='archivoprueba.csv'
    guardar(cliente,archivoprueba_csv)
    print(' GUARDADO EXITOSO...')
    pedidos.append(cliente)
    time.sleep(2)
    

def menuprincipal():
    limpiar()
    elmenu()
    acceso=1
    while acceso==1:
        try:
            opc=int(input(' Ingresa tu opcion (1-4) :         '))
        except ValueError:
            print(' Opcion equivocada, reintente nuevamente ')
            continue
        if opc==1:
            time.sleep(0.7)
            limpiar()
            registrarpedido()
            deseasseguir()
        elif opc==2:
            time.sleep(0.7)
            limpiar()
            listarpedidos()
            deseasseguir()
        elif opc==3:
            time.sleep(0.7)
            limpiar()
            imprimirhojaderuta()
            deseasseguir()
        elif opc==4:
            print('MUchas gracias ')
            quit()
        else:
            time.sleep(0.7)
            print('Opcion equivocada, intente nuevamente')
            
menuprincipal()