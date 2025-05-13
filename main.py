from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO("yolo11n.pt")

# Export the model to ONNX format
model.export(format="onnx") # creates 'yolo11n.onnx'

# Load the exported ONNX model
onnx_model = YOLO("yolo11n.onnx")

# Run inference on an example image
results = onnx_model.predict("https://ultralytics.com/images/bus.jpg")

# Print the results
print(results)