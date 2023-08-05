import requests
import pandas as pd
import os
import csv


def is_Unnamed0_id_bacha():
    pass

def is_Unnamed4_name_bacha():
    pass

def is_Unnamed18_price_bacha():
    pass

def no_hay_huecos(df):
    if not df.isnull().values.any():
        return True

def aplicar_recargo(df, gan):
    mod = (100 + gan) / 100
    df_aumentado = df['precio_bacha'] * mod
    return df_aumentado

def conseguir_lista_bacha():
    """
    Esta funcion devuelve la lista del bacha en formato
    id_bacha, name_bacha, precio_bacha
    """


    #Esta porcion consigue la ultima lista de precios a partir de un link fijo
    r = requests.get('https://www.elbacha.com.ar/Listas/CDEBSA_LISTA_2_PRECIOS.xls')
    with open('lista_bacha.xls', 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    
    #Aca se devuelve el df final listo para grabar en csv a partir de tomar las filas
    #que tengan un . en el codigo y si no hay NaN
    df_lista_bacha = pd.read_excel('lista_bacha.xls')
    os.remove('lista_bacha.xls')
    mask = df_lista_bacha['Unnamed: 0'].str.contains(pat = '[.]', na=False, regex=True)
    df_filtrado = df_lista_bacha.loc[mask]
    df_final = pd.concat([df_filtrado['Unnamed: 0'], df_filtrado['Unnamed: 4'], df_filtrado['Unnamed: 18']], axis = 1, keys=['id_bacha','name_bacha','precio_bacha'])
    if no_hay_huecos(df_final):
        print('la lista nueva conseguida tiene', df_final.shape[0], 'productos')
        return df_final
    else:
        print('chequear NaN')

def leer_clave():
    df = pd.read_excel('lucas.xlsx')
    return df

def leer_filtro():
    ids = pd.read_csv('D:\\cositas\\NeoClean_Actualizator\\claves\\id_bacha_filtro.csv')['id_bacha'].tolist()
    return ids

if __name__ == '__main__':

    lista_bacha = conseguir_lista_bacha()
    #print(aplicar_recargo(lista_bacha, 50))

    
    #clave = leer_clave()
    #clave.to_csv('clave_lucas.csv')
    ids = leer_filtro()
    filtered_df = lista_bacha[lista_bacha['id_bacha'].isin(ids)]
    print("Se encontraron", filtered_df.shape[0], "productos validos segun la clave")
    filtered_df.to_csv('../lista_bacha.csv')