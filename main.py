import cv2

def face_capture():

    cascade_path = r"C:\Users\Alex\Desktop\Education\SF\Project\SF_Project_1sem\filters\cascade.xml"

    video_path = r"C:\Users\Alex\Desktop\Education\SF\Project\SF_Project_1sem\videos\video1.mov"


    # Создание объекта классификатора для обнаружения лиц
    clt = cv2.CascadeClassifier(cascade_path)

    # Создание объекта видеокамеры с указанием пути к видеофайлу
    camera = cv2.VideoCapture(video_path)

    # Проверка успешного открытия видеофайла
    if not camera.isOpened():
        print("Ошибка: Не удалось открыть видеофайл.")
        return

    # Бесконечный цикл для обработки каждого кадра видео
    while True:
        # Чтение кадра из видеофайла
        ret, frame = camera.read()

        # Проверка наличия кадра и успешности его чтения
        if not ret:
            print("Ошибка: Не удалось прочитать кадр.")
            break

        # Преобразование цветного изображения в оттенки серого
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Обнаружение лиц на кадре
        faces = clt.detectMultiScale(
            gray,
            scaleFactor=1.01,
            minNeighbors=7,
            minSize=(150, 150),
            maxSize=(250,250)
        )

        # Отрисовка прямоугольников вокруг обнаруженных лиц
        for (x, y, width, height ) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)

        # Отображение обработанного кадра с лицами
        cv2.imshow("Лица", frame)

        # Выход из программы при нажатии клавиши 'q'
        key = cv2.waitKey(1)
        if key in (ord("q"), 27):  # 27 - ASCII код клавиши 'Esc'
            break

    # Освобождение ресурсов видеокамеры и закрытие окон OpenCV
    camera.release()
    cv2.destroyAllWindows()

# Основная функция, запускающая программу
def main():
    face_capture()

# Проверка, что программа запускается как самостоятельный скрипт
if __name__ == "__main__":
    main()
<<<<<<< HEAD



def checkpeoplt():
    pass
=======
