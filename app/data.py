# Gate 0 es no reserva
data = [{
    'DNI': '74624018', 'USUARIO': 'Javier iman',
    'Reserva': 1, 'Gate':1, 'time': '9:00pm', 'day': '10/11/2023'
},
{
    'DNI': '72671713', 'USUARIO': 'Cristhopher Atoche',
    'Reserva': 0, 'Gate':0
},
{
    'DNI': '77654321', 'USUARIO': 'Pepito Perez',
    'Reserva': 1, 'Gate':2, 'time': '8:00pm', 'day': '10/11/2023'
}]

times = [{'day': '10/11/2023', 'times':[{'time':'8:00 pm','gates':[{'gate':1,'reserva':0},{'gate':2,'reserva':1}]}]},
         {'day': '11/11/2023', 'times':[{'time':'8:00 pm','gates':[{'gate':1,'reserva':1},{'gate':2,'reserva':0}]}]}]