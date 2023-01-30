import torch as t

a = t.randint(0,2,(20,2))
b = (a.sum(dim=1) == 1).to(t.long)

data = a[b == 1]
data = a[b == 0]
print(data)