

import pytorch
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "c")

t1 = torch.Tensor([1,2,3])
print(t1)