from ultralytics import YOLO
import cv2
import numpy as np
target_size = (640, 640) 
print("load model")

# Open the video file
video_path = 0
cap = cv2.VideoCapture(video_path)
def anaylze_frame(frame):
    # original image scale
    h, w = frame.shape[:2]
    # analyze the chessboard corners and resize to 640x640
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # blur the image to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (7, 7), None)
    if ret:
        # modify the corners to match the 640x640 image
        scale_x = target_size[0] / w
        scale_y = target_size[0] / h
        
        scaled_corners = corners.copy()   
        scaled_corners[:, :, 0] *= scale_x
        scaled_corners[:, :, 1] *= scale_y   
        #scaled_corners = scaled_corners.reshape(-1, 1, 2)

        return ret,scaled_corners
    else:
        return ret,corners
model = YOLO("F:\\ViChess\\ObjectDetection\\Traindataset\\runs\\detect\\train\\weights\\best.pt")
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        # results = model.track(frame, persist=True)
       
        resized_image = cv2.resize(frame, target_size)
        results = model(resized_image)
        res_frame = results[0].plot()
        
        ret,corners = anaylze_frame(frame)
        if ret:
            # Draw and display the corners
            res_frame = cv2.drawChessboardCorners(res_frame, (7, 7), corners, ret)

        
        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", res_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
# cap.release()
# # Load the trained model
# model = YOLO("F:\\ViChess\\ObjectDetection\\Traindataset\\runs\\detect\\train\\weights\\best.pt")
# print("process")
# image = cv2.imread("F:\\ViChess\\ObjectDetection\\Traindataset\\mychess5.jpg")
# resized_image = cv2.resize(image, target_size)
# results = model(resized_image)
# print("show results")
# results[0].show()