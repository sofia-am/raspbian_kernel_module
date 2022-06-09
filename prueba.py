import numpy as np
from itertools import count
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, (ax1) = plt.subplots(1,1)
x_data, y1_data  =[], []
time1 = 0
line, = ax1.plot([], [], lw=7, color ='r') 

def set_figure():
    
    fig.set_size_inches(6,4)
    fig.suptitle('Sensado de Temperatura-Humedad', fontsize=10 , color='red')

    ax1.set_title('Sensor de humedad',fontdict={'color':'red','weight':'bold','size' : 5}, pad=14)
    ax1.set_xlabel('Tiempo[s]',fontdict={'color':'white','weight':'bold','size' : 10})
    ax1.set_ylabel('Humedad [%]',fontdict={'color':'white','weight':'bold','size' : 14})
     
    ax1.tick_params(axis='both', which='major', labelsize=14)
    ax1.tick_params(axis='both', which='minor', labelsize=12)
    ax1.set_yticks(np.arange(0, 35, 5))
    ax1.set_xticks(np.arange(0, 60, 10))

DEVICE_FILE = "/dev/SdeC_drv4"

def write(channel):    
    
    file = open(DEVICE_FILE, "w")
    file.write(channel)
    file.close()


def read_sensor():
    #cat
    file = open(DEVICE_FILE,"r")
    value = file.read()
    file.close()

    return value


def graficar(self):
    global time1
    time1 += 3
    valor1 = read_sensor()
    x_data.append(time1)
    y1_data.append(valor1)
    print("Valor: ",valor1)        
    line.set_data(x_data, y1_data) 
    return line


valor = input("ingrese un valor: ")
write(valor)
read_sensor()
set_figure()
animacion = animation.FuncAnimation(fig, graficar, interval=3000)
plt.show()


  
    
