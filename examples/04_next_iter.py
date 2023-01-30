import torch as t 
import torch.utils.data as data

class XORDataset(data.Dataset):
    
    def __init__(self, size, std=0.1):
        super().__init__()
        """
        Inputs:
            size - Number of data points we want to generate
            std  - Standard deviation of the noise (see genterate_continuous_xor function)
        """
        self.size = size
        self.std  = std
        self.generate_continuous_xor()

    def generate_continuous_xor(self):
        # Each data point in the XOR dataset has two variables, x and y, that can be either 0 or 1
        # The label is their XOR combination, i.e 1 if only x or only y is 1 while the other is 0.
        # If x=y, the label is 0.
        data  = t.randint(low=0, high=2, size=(self.size,2), dtype=t.float32)
        label = (data.sum(dim=1) == 1).to(t.long)
        # To make it slightly more challenging, we add a bit of gaussian noise to the data points.
        data += self.std * t.randn(data.shape)

        self.data  = data
        self.label = label

    def __len__(self):
        # Number of data point we have, Alternatively self.data.shape[0], or self.label.shape[0]
        return self.size

    def __getitem__(self, idx) :
        # Return the idx-th data point of the dataset
        # If we have multiple things to return (data point and label), we can return them as tuple
        data_point = self.data[idx]
        data_label = self.label[idx]

        return data_point, data_label

dataset = XORDataset(size=200)

data_loader = data.DataLoader(dataset, batch_size=8, shuffle=True)

data_inputs, data_labels = next(iter(data_loader))

print("-"*100)
print(iter(data_loader))

# print("-"*100)
# print("Data inputs", data_inputs.shape, "\n", data_inputs)
# print("Data labels", data_labels.shape, "\n", data_labels)