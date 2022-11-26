"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    with open('clusters_report.txt') as data:
        data = data.readlines()

    registro = [[], [], [], []]

    cont = 0
    d = ''
    for dato in data:
        cont += 1
        if cont > 4:
            fila = dato.split() 
            if len(fila) != 0:
                if fila[0].isdigit():
                    a = int(fila[0])
                    b = int(fila[1])
                    c = float(fila[2].replace(',','.'))
                    if d !='':
                        registro[3].append(d[:-1].replace('.',''))
                        d = ''
                        for i in range(4, len(fila)):
                            d += fila[i] + ' '
                    else:
                        for i in range(4, len(fila)):
                            d += fila[i] + ' '
                    registro[0].append(a)
                    registro[1].append(b)
                    registro[2].append(c)
                else:
                    for i in range(len(fila)):
                        d += fila[i] + ' '
    
    registro[3].append(d[:-1].replace('.',''))
    df = pd.DataFrame(
        {
            "cluster": registro[0],
            "cantidad_de_palabras_clave": registro[1],
            "porcentaje_de_palabras_clave": registro[2],
            "principales_palabras_clave": registro[3],
        }
    )
    return df
