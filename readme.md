# Docker compose file for tensor rt support container with ultralytics YOLO example

Setting up:
- Build the docker image:
```
docker compose build
```
- Run empty container
```
docker compose up -d
```
- Shell into container
```
docker exec -it tensorrt bash
```
- Copy ultralytics .pt file to this repo edit model path in yolo_2_tensorry.py

- Run convert script from .pt to .engine (inside container bash)
```
python3 yolo_2_tensorry.py
```
- Test inference with single image
```
python3 run.py
```


