import torch
from torch import nn

# XOR data: a small example that needs a hidden layer.
X = torch.tensor([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y = torch.tensor([[0.], [1.], [1.], [0.]])

model = nn.Sequential(
    nn.Linear(2, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
    nn.Sigmoid()
)

loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.05)

for epoch in range(3000):
    output = model(X)
    loss = loss_fn(output, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    print("Predicted probabilities:\n", model(X))
    print("Predicted classes:\n", (model(X) >= 0.5).int())
