import requests
import json
#Funciones seleccionables por el usuario
from get import get
from post import post
from put_patch import put_patch
from delete import delete

print("Bienvenido a la API de prueba de Marthy")

url = "https://first-api-test-project.onrender.com/api/projects/"


#INTERFAZ INICIAL
def ui():
    
    print("""
¿Qué desea realizar?
1. Leer registros
2. Publicar un nuevo registro
3. Modificar un registro
4. Eliminar un registro""")
    
    action_u_response = input("""
Escriba la función que desea usar: """)
    
    #Comprobación para que que el usuario escriba una opción adecuada
    
    while action_u_response not in ["1", "2", "3", "4"]:
        print("""
Por favor escriba una opción válida (1, 2, 3 o 4)""")
        
        action_u_response = input("""
Escoja una opción válida: """)
    
    #Ejecución de la opción elejida
    if action_u_response == "1":
        get(url)
    elif action_u_response == "2":
        post(url)
    elif action_u_response == "3":
        put_patch(url)
    elif action_u_response == "4":
        delete(url)
    
    ui()

ui()

