# Base image with CUDA, cuDNN, and TensorRT already installed
FROM nvcr.io/nvidia/tensorrt:24.05-py3

# Install system dependencies required for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    libsm6 \
    libice6 \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    python3-opencv

# Set up working directory
WORKDIR /app

RUN pip install uv

COPY requirements.txt .
# Install dependencies from requirements.txt
RUN uv pip install --no-cache-dir -r requirements.txt --system

# Copy your Python inference script and model
COPY . .

# Default command
CMD ["python", "main.py"]