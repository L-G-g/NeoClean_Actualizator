import requests
import os
import pandas as pd

def conseguir_lista_bacha():
    """
    Esta función devuelve la lista del bacha en formato
    id_bacha, name_bacha, precio_bacha
    """

    # Esta porción consigue la última lista de precios a partir de un link fijo
    r = requests.get('https://www.elbacha.com.ar/Listas/CDEBSA_LISTA_2_PRECIOS.xls')
    subfolder = "Lista_vieja"
    
    # Create the subfolder if it doesn't exist
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)
    
    # Save the file in the subfolder
    file_path = os.path.join(subfolder, 'lista_bacha.xls')
    with open(file_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

    # Delete the oldest .xls file.
    xls_files = [f for f in os.listdir(subfolder) if f.endswith('.xls')]
    if len(xls_files) > 1:
        oldest_file = min(xls_files, key=lambda f: os.path.getctime(os.path.join(subfolder, f)))
        os.remove(os.path.join(subfolder, oldest_file))

    return file_path

if __name__ == '__main__':
    lista_bacha = conseguir_lista_bacha()
    print("La lista vieja se a actualizado a la ultima lista disponible")
