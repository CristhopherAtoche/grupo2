import data
import datetime as dt
bd = data.data
times = data.times

def search(dni):
    var_return = False
    for dato in bd:
        if dato['DNI'] == dni:
            print("DNI Encontrado")
            var_return = True
            return var_return
        
        else:
            print("DNI no encontrado")
            return False


def val_dnitype(dni):
    for i, dato in enumerate(bd):
        if dato['DNI'] == dni:
            print("DNI Encontrado")
            return i, dato
    print("DNI no encontrado")
    return None, None


def reserved_gate(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            gate = dato['Gate']
        return gate


def have_permission(dni):
    for dato in bd:
        if dato ['DNI'] == dni:
            access = dato['Reserva']
        else:
            return access

def day_():
    x = dt.date.today()
    x_str = f'{x.day}/{x.month}/{x.year}'
    return x_str

def time():
    hour_ = dt.datetime.now()
    if int(hour_.hour)>12:
        str_hour = f'{hour_.hour-12}:00pm'
    elif int(hour_.hour)<12:
        str_hour = f'{hour_.hour}:00am'
    else:
        str_hour = f'{hour_.hour}:00m'
    return str_hour

def val_gate(day,time):
    #DEVUELVE LA PRIMERA PUERTA ENCONTRADA
    for day in times:
        if day['day'] == day:
            for time in day['times']:
                if time['time'] == time:
                    for gate in time['gates']:
                        if gate ['reserva'] == 0:
                            gate = gate['gate']
        break
    if gate == None:
        gate = 0
    return gate


def available_gate():
    day = day()
    _time = time()
    return val_gate('10/11/2023','9:00pm')


def dni_read(dni):
    print("leyendo dni")
    index, user_data = val_dnitype(dni)  # PUEDE SER 0 o 1
    if index is not None:
        gate = user_data.get('Gate', 0)  # PUERTA O CANCHA
        access = user_data.get('Reserva', 0)  # ¿TIENE ACCESO?
        return [access, gate, index, user_data]
    else:
        print('Usted no tiene acceso')
        return [0, 0, None, None]


def update_gate_status(index, gate_status):
    bd[index]['Gate'] = gate_status

def reservation_now():
    ava_g = available_gate()  # HABRA UNA PUERTA DISPONIBLE?
    # SI NO HAY PUERTA DISPONIBLE SERA 0
    if ava_g == 0:
        print("NO HAY PUERTA DISPONIBLE")
        return [0, 0, None, None]
    else:
        return [ava_g, 1, None, None]
    print("Reserva ahora")
