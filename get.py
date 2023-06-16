import requests
import json

def get(url):
    print("""
Usted puede: 
1. Consultar todos los registros de la base de datos
2. Consultar un registro por su id
3. Volver al menú principal""")
    
    action_u_response = input("""
Escoja una opción: """)
    
    #Comprobación para que que el usuario escriba una opción adecuada
    
    while action_u_response not in ["1", "2", "3"]:
        print("""
Por favor escriba una opción válida (1, 2 o 3)""")
        
        action_u_response = input("""
Escoja una opción: """)
    
    #Ejecución de la acción 1 (Consultar todos los registros de la base de datos)
    if action_u_response == "1":
        
        #SOLICITUD A LA API
        
        request = requests.get(url)

        print("""
Usted ha escogido consultar todos los registros de la base de datos, son los siguientes:""")
        
        response = json.loads(request.text)
        
        #Impresión de todos los registros
        
        if request.status_code == 200:
            for i in response:
                print(f"""
Id: {i["id"]}
Title: {i["title"]}
Description: {i["description"]}
Techonology: {i["technology"]}
Created at: {i["created_at"]}
""")
        else:
            print(f"""
Parece que ha ocurrido un error (status code {request.status_code})
Por favor intentelo de nuevo""")

    #Ejecución de la acción 2 (Consultar un registro por su id)
    
    elif action_u_response == "2":
        
        get_element = input("""
Escriba el id del elemento que desea consultar: """)
        
        #SOLICITUD A LA API
        
        request = requests.get(f"{url}{get_element}")
        
        #Comprobación de que el registros escogido se encuentre en la base de datos
        
        while request.status_code == 404 or get_element == "":
            print(f"""
El id que solicitó no se encuentra en la base de datos.
""")
            get_element = input("Por favor ingrese un id válido: ")

            #SOLICITUD A LA API
            
            request = requests.get(f"{url}{get_element}")
        
        response = json.loads(request.text)
        
        #Impresión del registro escogido por el usuario
        
        if request.status_code == 200:
            print(f"""
Id: {response["id"]}
Title: {response["title"]}
Description: {response["description"]}
Techonology: {response["technology"]}
Created at: {response["created_at"]}
""")
        else:
            print(f"""
Parece que ha ocurrido un error (status code {request.status_code})
Por favor intentelo de nuevo""")
            

    input("""
Presione ENTER para volver al menú principal... """)

    print("""
----VOLVIENDO AL MENÚ PRINCIPAL----


""")