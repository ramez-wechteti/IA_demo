FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY *.py *.jpg *.names *.txt /app/ 

# Update the package repositories
RUN apt-get update && apt-get install -y git

# Install your Python code dependencies
RUN pip install -r requirements.txt
# Install YOLOv5
RUN git clone https://github.com/ultralytics/yolov5.git && \
  cd yolov5 && \
  pip install -r requirements.txt

RUN mkdir /app/output

# Run the application
#CMD ["ls", "-lrt"]
CMD ["python", "demo.py"]
