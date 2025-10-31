import time
from ultralytics import YOLO
import cv2

image_path = "bus.png"

# Load models
yolo_pt = YOLO("yolo11n.pt")          # PyTorch model
yolo_trt = YOLO("yolo11n.engine")     # TensorRT engine

# Read image
image = cv2.imread(image_path)

# -------- PyTorch inference --------
start = time.time()
results_pt = yolo_pt(image)
end = time.time()
print(f"PyTorch YOLO11 inference time: {end - start:.3f} s")

# -------- TensorRT inference --------
start = time.time()
results_trt = yolo_trt(image)
end = time.time()
print(f"TensorRT YOLO11 inference time: {end - start:.3f} s")

# -------- Show annotated result for TensorRT --------
annotated_img = results_trt[0].plot()
cv2.imwrite("tensorrt_yolo_inference.png", annotated_img)
# cv2.imshow("TensorRT YOLO Inference", annotated_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
