import cv2
from yolov5.detect import detect

# Read class names from coco.names file
with open('coco.names', 'r') as file:
    classes = [line.strip() for line in file.readlines()]

# Read the image
image_path = "france.jpg"
frame = cv2.imread(image_path)

# Convert BGR to RGB
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Perform inference using YOLOv5
results = detect(source=frame, weights='yolov5s.pt', img_size=640, conf_thres=0.5, iou_thres=0.5)

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

# Convert RGB to BGR for saving the image
output_image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# Save the output image
output_image_path = "output/output_image.jpg"
cv2.imwrite(output_image_path, output_image)

print(f"Output image saved to {output_image_path}")
