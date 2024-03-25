import cv2
import numpy as np
import torch

# Load YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load COCO class names
classes = model.names

# Read the image
image_path = "image.jpg"
frame = cv2.imread(image_path)

# Convert BGR to RGB
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Perform inference
results = model(frame)

# Process results
for detection in results.xyxy[0]:
    class_id = int(detection[5])
    confidence = float(detection[4])

    if confidence > 0.5:
        x1, y1, x2, y2 = map(int, detection[:4])
        label = classes[class_id]
        
        color = (0, 255, 0)  # Default color (Green)
        if "ball" in label.lower():  # Check if label contains "ball"
            color = (0, 0, 255)  # Red for sports ball
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Convert RGB to BGR for display
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# Display the result
cv2.imshow("Object Detection", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
