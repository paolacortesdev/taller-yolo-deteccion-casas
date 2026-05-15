from ultralytics import YOLO

# cargar modelo entrenado
model = YOLO("models/house-yolo.pt")

# hacer predicción
results = model("test.jpg", show=True, conf=0.025)

# guardar resultados
results[0].save(filename="resultado5.jpg")

print("Predicción completada")