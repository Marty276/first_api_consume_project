import requests
import json

def post(url):
    
    print("""
A continuación, escriba la información del nuevo registro a subir...""")
    
    #Solicitud de la información del registro a subir
    
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
    
    request = requests.post(url, data = data_json, headers = headers)
    
    response = json.loads(request.text)
    
    #Impresión del registro subido en caso de éxito
    
    if request.status_code == 201:
        print(f"""
Su registro se ha publicado con éxito y está guardado como:
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