import os
import time
import urllib.request

import cv2 as cv
from mediapipe.tasks.python.core import base_options
from mediapipe.tasks.python.vision import (drawing_utils, face_detector,
                                           hand_landmarker)
from mediapipe.tasks.python.vision.core import image as mp_image
from mediapipe.tasks.python.vision.core import vision_task_running_mode


def download_model_if_missing(local_path: str, url: str):
    if not os.path.exists(local_path):
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        print(f'Baixando modelo: {url} -> {local_path}')
        urllib.request.urlretrieve(url, local_path)


def main():
    webcam = cv.VideoCapture(0)
    if not webcam.isOpened():
        print('Não foi possível acessar a webcam.')
        return

    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    hand_model_path = os.path.join(models_dir, 'hand_landmarker.task')
    face_model_path = os.path.join(
        models_dir, 'face_detection_short_range.tflite'
    )

    download_model_if_missing(
        hand_model_path,
        'https://storage.googleapis.com/mediapipe-tasks/hand_landmarker/hand_landmarker.task',
    )
    download_model_if_missing(
        face_model_path,
        'https://storage.googleapis.com/mediapipe-tasks/face_detector/face_detection_short_range.tflite',
    )

    hand_options = hand_landmarker.HandLandmarkerOptions(
        base_options=base_options.BaseOptions(
            model_asset_path=hand_model_path
        ),
        running_mode=vision_task_running_mode.VisionTaskRunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    face_options = face_detector.FaceDetectorOptions(
        base_options=base_options.BaseOptions(
            model_asset_path=face_model_path
        ),
        running_mode=vision_task_running_mode.VisionTaskRunningMode.VIDEO,
        min_detection_confidence=0.5,
    )

    hand_localizer = hand_landmarker.HandLandmarker.create_from_options(
        hand_options
    )
    face_localizer = face_detector.FaceDetector.create_from_options(
        face_options
    )

    # Criar a janela apenas uma vez antes do loop
    window_name = 'Reconhecimento de Rosto e Mão'
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    print("Pressione 'q' ou ESC para sair.")
    frame_count = 0

    def is_fist(landmarks):
        # Critério simples: todas as pontas dos dedos (8, 12, 16, 20) estão abaixo dos nós médios (6, 10, 14, 18) no eixo y
        # (para imagem não invertida, y aumenta para baixo)
        tips = [8, 12, 16, 20]
        mids = [6, 10, 14, 18]
        closed = 0
        for tip, mid in zip(tips, mids):
            if landmarks[tip].y > landmarks[mid].y:
                closed += 1
        return closed == 4

    foto_salva = False
    pasta_img = os.path.join(os.path.dirname(__file__), 'IMG')
    if not os.path.exists(pasta_img):
        os.makedirs(pasta_img)
    try:
        while True:
            ret, frame = webcam.read()
            if not ret:
                print('Falha ao capturar imagem.')
                break

            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            mp_img = mp_image.Image(mp_image.ImageFormat.SRGB, frame_rgb)
            timestamp_ms = int(time.time() * 1000)

            face_result = face_localizer.detect_for_video(mp_img, timestamp_ms)
            if face_result.detections:
                for detection in face_result.detections:
                    drawing_utils.draw_detection(frame, detection)

            hand_result = hand_localizer.detect_for_video(mp_img, timestamp_ms)
            fist_detected = False
            if hand_result.hand_landmarks:
                for hand_landmarks in hand_result.hand_landmarks:
                    drawing_utils.draw_landmarks(
                        frame,
                        hand_landmarks,
                        hand_landmarker.HandLandmarksConnections.HAND_CONNECTIONS,
                    )
                    # Detecta punho fechado
                    if is_fist(hand_landmarks):
                        fist_detected = True

            # Salva a foto apenas quando fechar a mão (punho fechado)
            if fist_detected and not foto_salva:
                nome_arquivo = os.path.join(
                    pasta_img, f'foto_punho_{int(time.time())}.jpg'
                )
                cv.imwrite(nome_arquivo, frame)
                print(f'Foto salva: {nome_arquivo}')
                foto_salva = True
            elif not fist_detected:
                foto_salva = False

            cv.imshow(window_name, frame)

            # Aguarda 30ms por uma tecla (corresponde a ~30 FPS)
            key = cv.waitKey(30) & 0xFF
            if key == ord('q') or key == 27:  # 27 é ESC
                print('Saindo...')
                break

            frame_count += 1
    finally:
        print('Finalizando...')
        hand_localizer.close()
        face_localizer.close()
        webcam.release()

        # Fechar a janela específica
        try:
            cv.destroyWindow(window_name)
        except:
            pass

        cv.destroyAllWindows()
        print(f'Total de frames processados: {frame_count}')
        print('Aplicação encerrada com sucesso.')


if __name__ == '__main__':
    main()
