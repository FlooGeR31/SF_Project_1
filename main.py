import cv2
import streamlit as st


cascade_path = "filters/cascade.xml"
video_path = "data/video1.mp4"


def face_capture():
    st.set_page_config(page_title="Streamlit + OpenCV приложение")
    st.title("Steamlit приложение")
    st.caption("OpenCV, Streamlit")

    frame_placeholder = st.empty()
    stop_button_pressed = st.button("Stop")

    # Создание объекта классификатора для обнаружения лиц
    clt = cv2.CascadeClassifier(cascade_path)

    # Создание объекта видеокамеры с указанием пути к видеофайлу
    camera = cv2.VideoCapture(video_path)

    # Проверка успешного открытия видеофайла
    if not camera.isOpened():
        print("Ошибка: Не удалось открыть видеофайл.")
        return

    # Бесконечный цикл для обработки каждого кадра видео
    while True and not stop_button_pressed:
        # Чтение кадра из видеофайла
        ret, frame = camera.read()

        # Проверка наличия кадра и успешности его чтения
        if not ret:
            st.write("Видео закончилось.")
            print("Ошибка: Не удалось прочитать кадр.")
            break

        # Преобразование цветного изображения в оттенки серого
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Обнаружение лиц на кадре
        faces = clt.detectMultiScale(
            frame,
            scaleFactor=1.22,
            minNeighbors=7,
            minSize=(80, 80),
            maxSize=(240, 240)
        )

        # Отрисовка прямоугольников вокруг обнаруженных лиц
        for (x, y, width, height) in faces:
            cv2.rectangle(frame,
                          (x, y),
                          (x + width, y + height),
                          (0, 0, 255),
                          2)

        # Отображение обработанного кадра с лицами
        frame_placeholder.image(frame, channels='BGR')
        # cv2.imshow("Лица", frame)

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


if __name__ == "__main__":
    main()
