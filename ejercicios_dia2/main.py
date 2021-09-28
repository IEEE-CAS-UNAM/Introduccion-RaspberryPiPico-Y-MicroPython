from machine import Pin#La clase Pin de machine nos sirve para gestionar u manipular los GPIO de la raspberry Pi PICO
from utime import sleep_ms#El modulo utime sirve para trabajar con tiempo, en este caso milisegundos

#Zona de declaración de funciones y variables, además es el código que se ejecuta 1

l1 = Pin(16, Pin.OUT)#Declaramos el pin digital como salida
l2 = Pin(17, Pin.OUT)#Declaramos el pin digital como salida
l3 = Pin(18, Pin.OUT)#Declaramos el pin digital como salida
l4 = Pin(19, Pin.OUT)#Declaramos el pin digital como salida

led = Pin(25, Pin.OUT)#Declaramos el pin digital como salida

boton = Pin(20, Pin.IN, Pin.PULL_UP)#Declaramos el pin digital como entrada, además tiene una config pull-up

tiempo_max = 10

tiempo_min = 30

paso = [
    #columnas:
    #0 1 2 3
    [1,0,0,0], #fila 0
    [1,1,0,0], #fila 1
    [0,1,0,0], #fila 2
    [0,1,1,0], #fila 3
    [0,0,1,0], #fila 4
    [0,0,1,1], #fila 5
    [0,0,0,1], #fila 6
    [1,0,0,1]  #fila 7
    ]

def giroAntiHorario(tiempo):
    for i in range(8):
        l1.value(paso[i][0])
        l2.value(paso[i][1])
        l3.value(paso[i][2])
        l4.value(paso[i][3])
        sleep_ms(tiempo)

def giroHorario(tiempo):
    for i in range(7,-1,-1):
        l1.value(paso[i][0])
        l2.value(paso[i][1])
        l3.value(paso[i][2])
        l4.value(paso[i][3])
        sleep_ms(tiempo)
    
def apagar():
    l1.value(0)
    l2.value(0)
    l3.value(0)
    l4.value(0)
    
def parpadeo():
    for i in range(30):
        led.on()
        sleep_ms(tiempo_min)
        led.off()
        sleep_ms(tiempo_min)
    
posicionActual = 0

while round(1.4222 * 10) > posicionActual:
    giroAntiHorario(tiempo_max)
    posicionActual = posicionActual + 1
    
while boton():
    giroHorario(tiempo_min)
    
posicionActual = 0

while round(1.4222 * 2) > posicionActual:
    giroHorario(tiempo_min)
    posicionActual = posicionActual + 1

posicionActual = 0

#Zona de código que se ejecuta por siempre
while True:
    
    try:
        nuevaPosicion = int(input("Ingresa la cantidad de grados: "))
        
        nuevaPosicion = round(1.4222 * nuevaPosicion)
        
        while nuevaPosicion > posicionActual:
            giroAntiHorario(tiempo_max)
            posicionActual = posicionActual + 1
            
        while nuevaPosicion < posicionActual:
            giroHorario(tiempo_max)
            posicionActual = posicionActual - 1
              
        apagar()
        
    except ValueError:
        parpadeo()

    

    