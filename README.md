# Detección de Casas usando YOLOv8

## Descripción
Proyecto de visión por computadora para detectar casas en imágenes colombianas utilizando YOLOv8.

## Dataset
El dataset fue construido manualmente utilizando imágenes urbanas y rurales de Colombia.  
Las anotaciones fueron realizadas en Roboflow utilizando bounding boxes.

Clases:
- houses

Enlace al dataset:
[Google Drive Dataset](https://drive.google.com/drive/folders/1oGiniFfYfnSLuGqxpnJYAqvt2ne0UMhb?usp=sharing)

## Estructura del proyecto

```bash
taller-yolo-casas/
│
├── dataset/
├── models/
├── src/
├── data.yaml
├── requirements.txt
└── README.md
```

## Entrenamiento

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar entrenamiento:

```bash
python src/train_yolo.py
```

## Inferencia

Ejecutar:

```bash
python src/inferencia.py
```

## Resultados

Métricas obtenidas:

- Recall: 1.0
- mAP50: 0.995
- mAP50-95: 0.446

El modelo logró detectar casas en imágenes de prueba, aunque presentó falsos positivos debido al tamaño reducido del dataset.

## Limitaciones

- Dataset pequeño
- Poca capacidad de generalización
- Sobreajuste en algunas imágenes

## Trabajo futuro

- Aumentar el número de imágenes
- Mejorar diversidad del dataset
- Ajustar hiperparámetros
- Probar modelos YOLO más grandes
