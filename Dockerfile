FROM python:3.12.2-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
#COPY *.py *.jpg *.names *.txt *.weights *.cfg *.pt /app/
COPY *.py *.jpg *.names *.txt /app/
COPY resources/images/ /app/
COPY resources/videos/ /app/ 

# Update the package repositories
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install your Python code dependencies
RUN pip install -r requirements.txt
# Install YOLOv5
#RUN git clone https://github.com/ultralytics/yolov5.git && \
#  cd yolov5 && \
#  pip install -r requirements.txt

RUN mkdir /app/output

# Run the application
#CMD ["ls", "-lrt"]
CMD ["python", "demo1.py"]
