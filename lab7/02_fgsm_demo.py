# Fast Gradient Sign Method (FGSM) demonstration.
import torch
from torch import nn

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 64),
    nn.ReLU(),
    nn.Linear(64, 10)
)

image = torch.rand(1, 1, 28, 28, requires_grad=True)
label = torch.tensor([3])
loss_fn = nn.CrossEntropyLoss()

output = model(image)
loss = loss_fn(output, label)
model.zero_grad()
loss.backward()

epsilon = 0.08
perturbation = epsilon * image.grad.sign()
adversarial_image = torch.clamp(image + perturbation, 0, 1)

print("Original prediction:", output.argmax(dim=1).item())
print("Adversarial prediction:",
      model(adversarial_image).argmax(dim=1).item())
print("Maximum pixel change:",
      (adversarial_image - image).abs().max().item())
