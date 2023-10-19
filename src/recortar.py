import cv2 as cv
import numpy as np
from keras.models import load_model

import random
numeros = []

def recortar (img):
  height, width, channels = img.shape

  w = int(width)
  h = int(height)


  img = img[int(h/2-125):int(h/2+125) , int(w/2-125):int(w/2+125)]
  
  return img



def generar(img):
    image = recortar(img)
    cv.waitKey(0)

    height, width, channels = image.shape

    # print(height)
    # print(width)

    widthToRect = 250 // 3  # En este caso, dividimos la imagen en un grid de 3x3


    COLORES = []
    for i in range(3):
      for j in range(3):
          start_x = j * widthToRect
          end_x = (j + 1) * widthToRect
          start_y = i * widthToRect
          end_y = (i + 1) * widthToRect

          # Recorta el bloque de la imagen original
          masked = image[start_y:end_y, start_x:end_x].copy()


          color1 = masked[random.randint(0, widthToRect-1) , random.randint(0, widthToRect-1)]
          color1 = (int(color1[0]) , int(color1[1]) , int(color1[2]))


          color2 = masked[random.randint(0, widthToRect-1) , random.randint(0, widthToRect-1)]
          color2 = (int(color2[0]) , int(color2[1]) , int(color2[2]))


          color3 = masked[random.randint(0, widthToRect-1) , random.randint(0, widthToRect-1)]
          color3 = (int(color3[0]) , int(color3[1]) , int(color3[2]))
          color4 = masked[random.randint(0, widthToRect-1) , random.randint(0, widthToRect-1)]
          color4 = (int(color4[0]) , int(color4[1]) , int(color4[2]))
          color5 = masked[random.randint(0, widthToRect-1) , random.randint(0, widthToRect-1)]
          color5 = (int(color5[0]) , int(color5[1]) , int(color5[2]))
          color6 = masked[random.randint(0, widthToRect-1) , random.randint(0, widthToRect-1)]
          color6 = (int(color6[0]) , int(color6[1]) , int(color6[2]))
          color7 = masked[random.randint(0, widthToRect-1) , random.randint(0, widthToRect-1)]
          color7 = (int(color7[0]) , int(color7[1]) , int(color7[2]))

          r =int( (color1[0] + color2[0] + color3[0] + color4[0] + color5[0] + color6[0] + color7[0]) / 7)
          g =int( (color1[1] + color2[1] + color3[1] + color4[1] + color5[1] + color6[1] + color7[1]) / 7)
          b =int( (color1[2] + color2[2] + color3[2] + color4[2] + color5[2] + color6[2] + color7[2]) / 7)


          COLORES.append((r , g , b))

          

    


    CUBO = np.zeros((300,300,3), np.uint8)
    index = 0

    for i in range(0 ,300 ,100 ):
        for j in range(0 ,300 , 100):
            cv.rectangle(CUBO,(i,j),(i+100,j+100),COLORES[index],-1)
            index+=1

    rotated_image = cv.rotate(CUBO, cv.ROTATE_90_CLOCKWISE)

  

    # cv.imshow('Imagen', image)
    # cv.imshow('Imagen', rotated_image)

    return CUBO

def recortar_img_cubo(imgs , name , name2):
    # print("aaaaaaaaaaaaaaaaaaaaa")
    small_size = 300//3
    n = 0
    small_images = []

    for i in range(3):
        for j in range(3):
            start_x = j * small_size
            end_x = (j + 1) * small_size
            start_y = i * small_size
            end_y = (i + 1) * small_size

            # Recorta el bloque de la imagen original
            masked = imgs[start_y:end_y, start_x:end_x].copy()

            small_images.append(masked)

    print(len(small_images))
    # Guarda y muestra las imágenes más pequeñas
    i = 0

    for imgsa in small_images :
        numero_aleatorio = random.randint(1, 10000)  # Genera un número aleatorio entre 1 y 100

        filename = f'img/predecir/img_{name2}_{i}.jpg'
        i+=1
        # cv.imshow('Imagen', imgsa)
        
        numeros.append(categorizar(imgsa))

        cv.imwrite(filename, imgsa)

loaded_model = load_model('./mi_modelo.h5')

def princiapal():
    for i in range(5):
        filename = 'img/images' + str(i+1) +'.jpg'
        filename2 = 'img/cara' + str(i+1) +'.jpg'
        cv.imwrite(filename2, generar(cv.imread(filename)))

        img = cv.imread(f'img/cara{i+1}.jpg')
        recortar_img_cubo(img , f'img/cara{i+1}.jpg' ,f'cara{i+1}' )

    return numeros


def categorizar(img):
  
  img = cv2.resize(img, (224,224))
  prediccion = modelo.predict(img.reshape(-1, 224, 224, 3))
  return np.argmax(prediccion[0], axis=-1)