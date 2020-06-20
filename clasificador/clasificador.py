import shutil, os

diccionario = {
    'jpg':'imagen',
    'jpeg':'imagen',
    'png':'imagen',
    'mp4':'video',
    'wav':'audio',
    'txt':'texto',
    'py':'texto',
    'java':'texto',
    'doc':'texto',
    'docx':'texto',
    'odt':'texto',
    'sql':'texto',
    'txt':'texto',
    'pdf':'texto',
    'nds':'juego'
}

origen = '' #ruta de origen
destino = '' #ruta de destino

while True:
    #lista de los archivos en la ruta origen
    ficheros = os.listdir(origen)
    #recorremos todos los ficheros y los movemos a la carpeta de destino
    for fichero in ficheros:
        try:
            #conseguimos la extension del archivo
            extension = fichero.split(".")[1]
            #lo movemos a la carpeta correspondiente
            shutil.move(origen + '/' + fichero, destino + '/' + diccionario[extension])
        except:
            #si el archivo es desconocido lo movemos a desconocido
            shutil.move(origen + '/' + fichero, destino + '/desconocido')