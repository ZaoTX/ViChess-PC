from ultralytics import YOLO
import onnx
import torch

torch.cuda.empty_cache()
# Load a model
model = YOLO("yolov8s.pt")

def train_model():
    # Train the model
    train_results = model.train(
        data="F:\\ViChess\\ObjectDetection\\Traindataset\\chess_pieces\\data.yaml",  # path to dataset YAML
        epochs=100,  # number of training epochs
        imgsz=416,  # training image size
        device=0,  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
        patience=7,
        batch=8 
    )

    # Evaluate model performance on the validation set
    metrics = model.val()
    torch.cuda.empty_cache()
    # Perform object detection on an image
    results = model("F:\\ViChess\\ObjectDetection\\Traindataset\\mychess.jpg")
    results[0].show()

    # Export the model to ONNX format
    path = model.export(format="onnx")  # return path to exported model

if __name__ == "__main__":
    train_model()