import torch

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

print("Tensor a:", a)
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Mean:", torch.mean(a))

# Autograd calculates the derivative automatically.
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x
y.backward()
print("dy/dx at x=2:", x.grad.item())
