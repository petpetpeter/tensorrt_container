from ultralytics import YOLO

model = YOLO("yolo11n.pt")
model.export(
    format="engine", 
    half=True, #FP16
)
# model.export(
#     format="engine", 
#     half=True,
#     imgsz=320
# )