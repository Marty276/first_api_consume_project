import requests
import json

def delete(url):

    get_element = input("""
Escriba el id del elemento que desea eliminar: """)
        
    #Petición GET para comprobar que exista y mostrar al usuario el registro a eliminar
    
    request = requests.get(f"{url}{get_element}")
    
    #Comprobación de que el registros escogido se encuentre en la base de datos
    
    while request.status_code == 404 or get_element == "":
        print(f"""
El id que solicitó no se encuentra en la base de datos.
""")
        get_element = input("Por favor ingrese un id válido: ")

        request = requests.get(f"{url}{get_element}")
        
    response = json.loads(request.text)
        
    if request.status_code == 200:
        
        #Muestra del elemento y comprobación antes de eliminarlo
        
        print(f"""
El registro a eliminar es el siguiente:
Id: {response["id"]}
Title: {response["title"]}
Description: {response["description"]}
Techonology: {response["technology"]}
Created at: {response["created_at"]}

¿Está seguro de que desea eliminar este elemento?""")
        
        action_u_response = input("""
1. Sí
2. No

Escoja una opción: """)
    
        #Comprobación para que que el usuario escriba una opción adecuada
    
        while action_u_response not in ["1", "2"]:
            print("""
Por favor escriba una opción válida (1 o 2)""")
        
            action_u_response = input("""
Escoja una opción: """)
    
        if action_u_response == "1":
            
            #SOLICITUD A LA API
            
            request = requests.delete(f"{url}{get_element}")
            
            if request.status_code == 204:
                print("""
El elemento ha sido eliminado con éxito""")
            else:
                print(f"""
Parece que ha ocurrido un error (status code {request.status_code})
Por favor intentelo de nuevo""")
        
    else:
        print(f"""
Parece que ha ocurrido un error (status code {request.status_code})
Por favor intentelo de nuevo""")
            

    input("""
Presione ENTER para volver al menú principal... """)

    print("""
----VOLVIENDO AL MENÚ PRINCIPAL----


""")