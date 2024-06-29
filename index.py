# Description: This script translates a given text from English to French and Zulu.
# Author: Fernando Rivera
# Asterki Dev "Spark Curiosity" - Microsoft Learn Student Ambassador Program

# Importar las bibliotecas necesarias
import requests  # Esta biblioteca nos ayuda a pedir cosas de internet
import uuid  # Esta biblioteca nos ayuda a crear un número único y aleatorio
import json  # Esta biblioteca nos ayuda a trabajar con datos en formato JSON (como un lenguaje que entienden las computadoras)
import dotenv  # Esta biblioteca nos ayuda a usar cosas del sistema, como las variables de entorno

config = dotenv.dotenv_values(".env")

# Guardar nuestras claves y endpoint del traductor (como nuestras contraseñas secretas)
key = config.get('TRANSLATOR_TEXT_SUBSCRIPTION_KEY')  # Nuestra clave secreta para usar el traductor
endpoint = config.get('TRANSLATOR_TEXT_ENDPOINT')  # El lugar en internet donde está el traductor
location = config.get('TRANSLATOR_TEXT_LOCATION')  # La región donde está nuestro traductor

# Definir el camino donde pedimos la traducción
path = '/translate'  # El camino que sigue nuestra solicitud
constructed_url = endpoint + path  # Juntar el lugar y el camino

# Configurar los parámetros de nuestra solicitud
params = {
    'api-version': '3.0',  # La versión de la API (como la versión del juego)
    'from': 'en',  # El idioma del texto original (inglés)
    'to': ['fr', 'zu']  # Los idiomas a los que queremos traducir (francés y zulú)
}

# Configurar los encabezados de nuestra solicitud
headers = {
    'Ocp-Apim-Subscription-Key': key,  # Nuestra clave secreta
    'Ocp-Apim-Subscription-Region': location,  # La región de nuestro traductor
    'Content-type': 'application/json',  # El tipo de contenido que estamos enviando
    'X-ClientTraceId': str(uuid.uuid4())  # Un número único y aleatorio para identificar nuestra solicitud
}

# Definir el cuerpo de nuestra solicitud (el texto que queremos traducir)
body = [{
    'text': 'I would really like to drive your car around the block a few times!'  # El texto en inglés que queremos traducir
}]

# Hacer la solicitud de traducción
request = requests.post(constructed_url, params=params, headers=headers, json=body)  # Pedir la traducción
response = request.json()  # Obtener la respuesta en formato JSON

# Mostrar la respuesta de la traducción
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))  # Imprimir la respuesta de forma bonita
