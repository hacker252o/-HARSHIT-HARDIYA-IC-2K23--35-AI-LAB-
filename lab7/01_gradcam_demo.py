# Small Grad-CAM demonstration on a generated image.
# It shows how gradients can highlight image regions used by a CNN.
import torch
from torch import nn
import torch.nn.functional as F

class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 8, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(8, 16, 3, padding=1),
            nn.ReLU()
        )
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Linear(16, 2)
        self.saved_features = None

    def forward(self, x):
        features = self.features(x)
        self.saved_features = features
        return self.classifier(self.pool(features).flatten(1))

model = SmallCNN()
image = torch.rand(1, 1, 16, 16)
scores = model(image)
class_id = scores.argmax(dim=1).item()

model.zero_grad()
scores[0, class_id].backward()
feature_maps = model.saved_features
weights = feature_maps.grad if feature_maps.grad is not None else None

# Retain gradients on the feature tensor before backward.
# Run forward again with retain_grad to collect them correctly.
model.zero_grad()
scores = model(image)
feature_maps = model.saved_features
feature_maps.retain_grad()
scores[0, class_id].backward()
weights = feature_maps.grad.mean(dim=(2, 3), keepdim=True)
heatmap = F.relu((weights * feature_maps).sum(dim=1, keepdim=True))
heatmap = F.interpolate(heatmap, size=(16, 16), mode="bilinear",
                        align_corners=False)
heatmap = heatmap / (heatmap.max() + 1e-8)

print("Predicted class:", class_id)
print("Grad-CAM heatmap shape:", tuple(heatmap.shape))
print("Heatmap values range:", heatmap.min().item(), "to", heatmap.max().item())
