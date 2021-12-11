import requests
from bs4 import BeautifulSoup

# Direccion url a hacer el login
url = "https://www.chess.com/login_and_go"

user = 'DavidSanchez123'
clave = 'David123Sanchez123'

# payload es un diccionario con los datos enviados mediante post
payload = {
    # En un simple login por lo general es:
    "Usuario": user,
    "Password": clave,
    "bntEntrar": 'login',
}

# Envia una peticion POST
response = requests.post(url, data=payload)

# Obtiene el estado de la respuesta a la peticion
estado = response.status_code

if estado == 200:

    s = requests.Session()
    print(s)
    r = s.post(url, data=payload)
    print('Inicio de sesion', str(r))
    print(r.status_code)

else:
    print("Error: " + str(estado) + "-> " + user + ":" + clave + "\n")

