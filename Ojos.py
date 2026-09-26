import cv2

modelo_rostros = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
camara = cv2.VideoCapture(0)
print("SISTEMA. Inicializando sensores visuales del robot.")
while True:
    ret, cuadro = camara.read()
    if not ret:
        break
    imagen_gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)
    rostros_detectados = modelo_rostros.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(rostros_detectados) > 0:
        print(f"Alerta! Objetivo detectado. Cantidad de rostros: {len(rostros_detectados)}")
        for x, y, ancho, alto in rostros_detectados:
            cv2.rectangle(cuadro, (x, y), (x + ancho, y + alto), (0, 255, 0), 2)
            centro_x = x + (ancho // 2)
            centro_y = y + (alto // 2)
            print(f"COMANDO ARDUINNO. centrar camara en coordenadas fisicas: X={centro_x}, Y{centro_y}")
    else:
        print("Escanenado perimetro... Sin noveades.")
    cv2.imshow("Camara de seguridad del robot", cuadro)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camara.release()
cv2.destroyAllWindows()
print("SISTEMA. Sensores apagados correctamente.")
