#Detectar si el usaruio estubo inactivo por más de 30 días

import datetime as dt

fecha_inicio_sesion = input("Último inicio de sesión en formato YYYY-MM-DD: ")
fecha_ingreso = dt.datetime.strptime(fecha_inicio_sesion, "%Y-%m-%d")

fecha_actual = dt.datetime.now()

print(fecha_inicio_sesion, fecha_actual)
