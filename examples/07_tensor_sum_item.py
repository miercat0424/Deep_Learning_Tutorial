import torch as t 
a = [i for i in range(30)]
b = t.Tensor(a)

print(b.sum())
print("*"*100)
print(b.sum().item())