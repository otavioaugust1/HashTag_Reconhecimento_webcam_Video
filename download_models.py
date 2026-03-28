#!/usr/bin/env python3
"""
Script para baixar os modelos pré-treinados do MediaPipe
Reconhecimento de Rosto e Mão
"""

import os
import urllib.request
from pathlib import Path


def download_model(url: str, output_path: str) -> bool:
    """Baixa um modelo se não existir"""
    if os.path.exists(output_path):
        print(f'✓ {output_path} já existe')
        return True

    print(f'Baixando: {url}')
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        urllib.request.urlretrieve(url, output_path)
        print(f'✓ Salvo em: {output_path}')
        return True
    except Exception as e:
        print(f'✗ Erro ao baixar: {e}')
        return False


def main():
    print('=' * 60)
    print('DOWNLOAD DOS MODELOS MEDIAPIPE')
    print('=' * 60)

    models_dir = os.path.join(os.path.dirname(__file__), 'models')

    # URLs dos modelos pré-treinados
    models = {
        'Face Detection': {
            'url': 'https://storage.googleapis.com/mediapipe-tasks/face_detector/face_detection_short_range.tflite',
            'path': os.path.join(
                models_dir, 'face_detection_short_range.tflite'
            ),
        },
        'Hand Landmarks': {
            'url': 'https://storage.googleapis.com/mediapipe-tasks/hand_landmarker/hand_landmarker.task',
            'path': os.path.join(models_dir, 'hand_landmarker.task'),
        },
    }

    print(f'\nPasta de destino: {models_dir}\n')

    success_count = 0
    for model_name, model_info in models.items():
        print(f'\n[{model_name}]')
        if download_model(model_info['url'], model_info['path']):
            success_count += 1

    print('\n' + '=' * 60)
    if success_count == len(models):
        print('✓ TODOS OS MODELOS BAIXADOS COM SUCESSO!')
        print('Você pode executar: python Reconhecimento_webCam.py')
    else:
        print(f'⚠ {success_count}/{len(models)} modelos baixados')
        print('Verifique sua conexão com a internet')
    print('=' * 60)


if __name__ == '__main__':
    main()
