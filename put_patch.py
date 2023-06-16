import requests
import json
def put_patch(url):
    
    print("""
Usted puede: 
1. Modificar todos los atributos de un registro
2. Modificar un único atributo de un registro
3. Volver al menú principal""")
    
    action_u_response = input("""
Escoja una opción: """)
    
    #Comprobación para que que el usuario escriba una opción adecuada
    
    while action_u_response not in ["1", "2", "3"]:
        print("""
Por favor escriba una opción válida (1, 2 o 3)""")
        
        action_u_response = input("""
Escoja una opción: """)
    
    get_element = input("""
Escriba el id del elemento que desea modificar: """)
    
    #Petición GET para comprobar que exista y mostrar al usuario el registro a editar

    p_request = requests.get(f"{url}{get_element}")
    
    #Comprobación de que el registros escogido se encuentre en la base de datos
    
    while p_request.status_code == 404 or get_element == "":
        print(f"""
El id que solicitó no se encuentra en la base de datos.
""")
        get_element = input("Por favor ingrese un id válido: ")

        p_request = requests.get(f"{url}{get_element}")

    p_response = json.loads(p_request.text)
    
    #Impresión del registro escogido
    
    print(f"""
Actualmente el registro se encuentra guardado como:
Id: {p_response["id"]}
Title: {p_response["title"]}
Description: {p_response["description"]}
Techonology: {p_response["technology"]}
Created at: {p_response["created_at"]}
""")

    if action_u_response == "1":
        
        print("""
A continuación, escriba la nueva información...""")
        
        #Solicitud de la información a editar
        
        data = {
            "title" : input("Title: "),
            "description" : input("Description: "),
            "technology" : input("Technology: ")
        }
        
        data_json = json.dumps(data)
        
        headers = {
            "Content-Type" : "application/json"
        }
        
        #SOLICITUD A LA API
        
        request = requests.put(f"{url}{get_element}/", data = data_json, headers = headers)

        response = json.loads(request.text)
        
        #Impresión del registro editado en caso de éxito
        
        if request.status_code == 200:            
            print(f"""
El registro ha sido modificado con éxito y está guardado como:
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
     
    elif action_u_response == "2":
         
        print("""
Usted puede editar los siguientes atributos:
1. Title
2. Description
3. Technology""")
        
        #Elección del atributo a editar
        
        action_u_response = input("""
Escoja una opción: """)
        
        #Comprobación para que que el usuario escriba una opción adecuada
        
        while action_u_response not in ["1", "2", "3"]:
            print("""
Por favor escriba una opción válida (1, 2 o 3)""")
        
            action_u_response = input("""
Escoja una opción: """)
        
        atributos = {
            "1" : ("title", "Title"),
            "2" : ("description", "Description"),
            "3" : ("technology", "Technology")
        }
        
        #Solicitud de la información a editar
        
        print("""
Ahora escriba el valor que asignará al atributo seleccionado
""")
        
        data = {
            atributos[action_u_response][0] : input(f"{atributos[action_u_response][1]}: "),
        }
        
        data_json = json.dumps(data)
        
        headers = {
            "Content-Type" : "application/json"
        }
        
        #SOLICITUD A LA API
        
        request = requests.patch(f"{url}{get_element}/", data = data_json, headers = headers)

        response = json.loads(request.text)
        
        #Impresión del registro editado en caso de éxito
        
        if request.status_code == 200:
            print(f"""
El registro ha sido modificado con éxito y está guardado como:
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