
import re
import os

def clean_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '_', filename).strip()

notas = {}

n=1
nombre_texto=""
with open('My Clippings.txt', 'r', encoding='utf-8') as file:
    for linea in file:
        if n<2273:
            if n%5==1:
                # print("1-"+linea)
                if linea not in notas:
                    notas[linea] = [[],[]]
                    nombre_texto = linea
            if n%5==2:
                # print("2-"+linea)
                notas[nombre_texto][1].append(linea)
            # if n%5==3:
            #     print("3-"+linea)
            if n%5==4:
                # print("4-"+linea)
                notas[nombre_texto][0].append(linea)
            # if n%5==0:
            #     print("5-"+linea)


        n=n+1

carpeta = "Notas"
os.makedirs(carpeta, exist_ok=True)


for clave, listas in notas.items():
    cleaned_clave = clean_filename(clave)
    ruta_archivo = os.path.join(carpeta, f'{cleaned_clave}.txt')

    with open(ruta_archivo, 'w', encoding='utf-8') as file:

        file.write(f'{clave}\n')
        # Obtener la longitud máxima de las listas internas
        max_length = max(len(lista) for lista in listas)
        # Iterar intercaladamente sobre los elementos de las listas internas
        for i in range(max_length):
            for lista in listas:
                if i < len(lista):
                    # print(f'  {lista[i]}')
                    file.write(lista[i])
                    if '-' in lista[i]:
                        file.write('\n')
                        


# with open('ordenamiento.txt', 'w') as file:
#     file.write('Hola, este es el contenido del fichero.\n')
#     file.write('Esta es una nueva línea.')
