import cv2
import torch
from pathlib import Path
from tqdm import tqdm

def process_video(video_path, output_path):
    # Load YOLOv5
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    names = model.module.names if hasattr(model, 'module') else model.names

    # Open video file
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print("Error: Could not open video file.")
        return

    # Get video properties
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Process each frame
    pbar = tqdm(total=int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Perform object detection
        results = model(frame)

        # Draw bounding boxes and labels
        for detection in results.xyxy[0]:
            x1, y1, x2, y2, conf, class_id = map(int, detection)
            label = names[class_id]
            color = (0, 0, 255) if label == 'ball' else (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Write the frame
        out.write(frame)
        pbar.update(1)

    # Release everything when done
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()
    pbar.close()

# Example usage
process_video('input_video.mp4', 'output_video.mp4')
