import cv2
import face_recognition

# Variable global para control de depuración
DEBUG = False

def log_debug(message):
    """Imprime mensajes de depuración si DEBUG es True."""
    if DEBUG:
        print(message)

def cargar_fichero(ruta):
    """Carga una imagen desde una ruta dada y devuelve la codificación del rostro."""
    log_debug("Cargando la imagen del DNI...")
    try:
        image = face_recognition.load_image_file(ruta)
        face_encoding = face_recognition.face_encodings(image)[0]
        log_debug("Imagen del DNI cargada y codificación de rostro obtenida.")
        return face_encoding
    except Exception as e:
        log_debug(f"Error al cargar la imagen del DNI o al obtener la codificación: {e}")
        exit()

# Cargar la imagen del DNI y obtener la codificación del rostro
dni_face_encoding = cargar_fichero("dni.jpg")

# Inicializar la captura de video desde la cámara
log_debug("Iniciando la captura de video...")
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Capturar un solo frame de video
    ret, frame = video_capture.read()

    if not ret:
        log_debug("Error: No se pudo capturar el frame de video.")
        break

    # Redimensionar el frame para un procesamiento más rápido (opcional)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convertir la imagen de BGR a RGB
    rgb_small_frame = small_frame[:, :, ::-1]

    # Encontrar todas las caras en el frame
    log_debug("Buscando caras en el frame...")
    try:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        log_debug(f"Se encontraron {len(face_locations)} cara(s) en el frame.")
    except Exception as e:
        log_debug(f"Error al buscar caras en el frame: {e}")
        break
    
    # Verifica si se encontraron rostros antes de intentar codificarlos
    if face_locations:
        log_debug("Codificando las caras encontradas...")
        try:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            log_debug(f"Codificaciones de {len(face_encodings)} cara(s) obtenidas.")
        except Exception as e:
            log_debug(f"Error al codificar las caras: {e}")
            break

        # Inicializar una variable para almacenar el resultado
        face_match = False

        for face_encoding in face_encodings:
            # Comparar la cara del video con la cara del DNI
            try:
                matches = face_recognition.compare_faces([dni_face_encoding], face_encoding)
                if True in matches:
                    face_match = True
                log_debug(f"Resultado de la comparación: {'Match' if face_match else 'No Match'}")
            except Exception as e:
                log_debug(f"Error al comparar las caras: {e}")
                break

        # Mostrar los resultados
        for (top, right, bottom, left) in face_locations:
            # Escalar las coordenadas de vuelta al tamaño original
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Dibujar un recuadro verde alrededor de la cara si hay coincidencia, rojo si no la hay
            color = (0, 255, 0) if face_match else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

            # Añadir una etiqueta sobre la cara
            label = "Match" if face_match else "No Match"
            cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Mostrar el frame con el recuadro en la ventana
    cv2.imshow('Video', frame)

    # Salir del bucle cuando se presiona la tecla 'q' o si se cierra la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        log_debug("Cerrando el programa...")
        break

# Liberar la captura de video y cerrar todas las ventanas
video_capture.release()
cv2.destroyAllWindows()
log_debug("Programa cerrado correctamente.")
