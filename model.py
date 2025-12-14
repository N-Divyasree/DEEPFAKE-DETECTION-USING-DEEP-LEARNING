import torch
import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights
from torchvision import transforms
from PIL import Image
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

BASE_DIR = os.path.dirname(os.path.abspath(_file_))
MODEL_PATH = os.path.join(BASE_DIR, "resnet18_deepfake.pth")

def load_model():
    model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    model.fc = nn.Linear(model.fc.in_features, 2)

    print("Loading model from:", MODEL_PATH)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))

    model = model.to(device)
    model.eval()
    return model

model = load_model()

transform_img = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

classes = ["real", "fake"]

def predict(img_path):
    img = Image.open(img_path).convert("RGB")
    img = transform_img(img).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(img)

        probs = torch.softmax(output, dim=1)
        confidence, pred_class = torch.max(probs, dim=1)

        label = classes[pred_class.item()]
        confidence = float(confidence.item())

    return {
        "prediction": label,
        "confidence": confidence
    }