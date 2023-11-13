import time
import data
from datetime import datetime
import reads

num_gate = 2
in_gate = 0  # INICIAREMOS LA PUERTA SI ESTA CERRADA

def access():
    dni = input('Ingrese DNI: ')
    reserve = reads.dni_read(dni)

    if reserve == [0, 0] and reads.search(dni) == False:
        print("El DNI no está en la base de datos")
        print("Ingrese un DNI que sí esté en la base de datos")
        return [0, 0]

    elif reserve == [0, 0] and reads.search(dni) == True:
        _action = input('Ingresa s o n para definir si quieres reservar ahora: ')
        if _action == 's':
            access_val = reads.reservation_now()[1]
            gate = reads.reservation_now()[0]
            if gate == 0:
                print("NO HAY CANCHA DISPONIBLE")
                print("NO SE ABRIRÁ NINGUNA PUERTA")
                return [0, 0]
        else:
            print("HA DECIDIDO QUE NO VA A RESERVAR")
            print("INICIANDO EL PROGRAMA.....")
            return [0, 0]

    else:
        access_val = reserve[0]
        gate = reserve[1]

    if gate != 0:
        print(f"ABRIENDO LA CANCHA {gate}")
        return [access_val, gate]
    else:
        print("ERROR: No se abrió ninguna puerta.")
        return [0, 0]

def save():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"GUARDANDO - Hora de ingreso: {current_time}")

def update_gate_status(index, gate_status):
    data.data[index]['Gate'] = gate_status
