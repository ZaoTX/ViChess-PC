import cv2

# Open the default webcam (usually webcam 0)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # Set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Set height
path = "Dataset4/"
# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Counter to name saved images uniquely
img_counter = 304

print("Press 'Space' to capture an image, and 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame is read correctly, ret will be True
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Display the resulting frame
    cv2.imshow("Webcam Feed", frame)

    # Wait for user input
    key = cv2.waitKey(1) & 0xFF

    # Press the spacebar to capture and save the image
    if key == ord(' '):
        img_name = f"captured_image_{img_counter}.png"
        cv2.imwrite(path+img_name, frame)
        print(f"{img_name} saved!")
        img_counter += 1

    # Press 'q' to exit the loop
    elif key == ord('q'):
        print("Exiting...")
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
