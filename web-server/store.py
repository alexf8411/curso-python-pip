import requests #importar la libreria request

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #obteniendo solicitud de la pagina con el api de platzi
    print(r.status_code) #obtiene el estado
    print(r.text) #informacion que responde el api
    print(type(r.text)) #tipo de dato que trae r.text es un string
    categories = r.json() #convertirlo en lista de formato json
    for category in categories: #iterando la categorias
        print(category['name']) # trae el listado de solo los names