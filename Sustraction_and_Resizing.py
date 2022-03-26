#%%
#https://www.remove.bg/api#sample-code
import requests
import os
import os.path
from resize_images import resizing
import shutil
from PIL import Image


def resizing(f,f_saved,x=80,y=80):
    """
    recibe dos rutas como parámetros, donde se encuentran las imágenes a utilizar
    y les realiza un resizing, ya hardcodeado en 50x50 pixels
    """
    for file in os.listdir(f):
        f_img = f + "/" + file
        f_img_save = f_saved + "/" + file
        img = Image.open(f_img)
        img = img.resize((x,y))
        f_img_save = f_img_save.strip(".jpg") + ".png" if ".jpg" in f_img_save else f_img_save
        img.save(f_img_save)
        shutil.move(r'Sin procesar' + '\\' + file,r'Ya usado y procesado' + '\\' + file )

f_SP = r'path\to\Imagenes\Sin procesar'
f_saved = r'path\to\Imagenes\Procesadas'



def extraction(archivo_conteo,api_key):
    """
    se recibe un archivo que lleva el conteo de la cantidad de veces que se usó la api
    máximo por cada key: 50
    la api hace una extracción del fondo, guardando el archivo en un path distinto
    del que recibe
    """
    with open(archivo_conteo,"r") as file0:
        data = int(file0.readline())
        print(data)
        
        for file1 in os.listdir(f_SE_SP):
            if data < 50:

                data += 1


                response = requests.post(
                    'https://api.remove.bg/v1.0/removebg',
                    files={'image_file': open(r'Sin Extraer y Sin procesar' + '\\' + file1, 'rb')},
                    data={'size': 'auto'},
                    headers={'X-Api-Key': api_key},
                )
                
                if response.status_code == requests.codes.ok:
                    with open(r'Sin procesar' + '\\' + file1 , 'wb') as out:
                        out.write(response.content)
                else:
                    print("Error:", response.status_code, response.text)
                
                with open(archivo_conteo, 'w+') as file2:
                    file2.write(str(data))

                shutil.move(r'Sin Extraer y Sin procesar' + '\\' + file1,r'Ya usado y procesado' + '\\' + file1 )

            else:
                raise Exception("se alcanzó el límite de 50 imágenes por mes de la API, usá otra cuenta de Gmail")




if __name__ == "__main__":
   
    try:
    
        api_key = "" # "yhXTdWvD1oLEKsVoTWW57GvB" ya gastada
        f_SE_SP = r'path\to\Imagenes\Sin Extraer y Sin procesar'
        f_SP = r'path\to\Imagenes\Sin procesar'
        f_saved = r'path\to\Imagenes\Procesadas'

        extraction("conteo.txt",api_key)

        resizing(f_SP,f_saved)

        
    
    except:
        raise Exception



