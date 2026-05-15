from ultralytics import YOLO

# cargar modelo entrenado
model = YOLO("models/house-yolo.pt")

# hacer predicción
results = model("results/test3.jpg", show=True, conf=0.025)

# guardar resultados
results[0].save(filename="results/resultado3.jpg")

print("Predicción completada")