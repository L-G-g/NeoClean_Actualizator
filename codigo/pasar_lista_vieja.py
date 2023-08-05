import requests
import pandas as pd
import os
import csv
import sys

def no_hay_huecos(df):
    if not df.isnull().values.any():
        return True



if __name__ == '__main__':
    # Set the folder path
    folder_path = r"D:\cositas\NeoClean_Actualizator\Lista_vieja"

    # Get the parent directory of the script
    #parent_dir = os.path.dirname(os.path.abspath(__file__))
    #folder_path = os.path.join(parent_dir, "Lista_vieja")
    # Get a list of files in the folder
    file_list = os.listdir(folder_path)

    # Filter the list to only include Excel files
    excel_files = [f for f in file_list if f.endswith('.xlsx') or f.endswith('.xls')]

    # Read the first Excel file in the folder
    if len(excel_files) > 1:
        print("Hay mas de una lista en la carpeta Lista vieja. Tiene que haber solo una")
        os._exit(0)
    elif len(excel_files) == 1:
        file_path = os.path.join(folder_path, excel_files[0])
        df = pd.read_excel(file_path)
        print("Una lista vieja encontrada!")
    else:
        print("No hay ninguna lista en la carpeta Lista vieja. Tiene que haber solo una")
        sys.exit()
    # Hace un curado de el df que viene de la carpeta 
    mask = df['Unnamed: 0'].str.contains(pat = '[.]', na=False, regex=True)
    df_filtrado = df.loc[mask]
    df_final = pd.concat([df_filtrado['Unnamed: 0'], df_filtrado['Unnamed: 4'], df_filtrado['Unnamed: 18']], axis = 1, keys=['id_bacha','name_bacha','precio_bacha'])
    df_final.to_csv('../lista_vieja.csv')