import torch
from torch import nn

# Sample relationship: y is approximately 3x + 2.
x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([[5.0], [8.0], [11.0], [14.0], [17.0]])

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    prediction = model(x)
    loss = loss_fn(prediction, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Learned weight:", model.weight.item())
print("Learned bias:", model.bias.item())
print("Prediction for x=6:", model(torch.tensor([[6.0]])).item())
