"""
Lab 01 - Exercise 01
Tensor Basics

Topics:
- Tensor creation
- Shape and dimensions
- Data types
- Element access
- Tensor conversion
- Memory behavior
- Device management
"""
from os import name

import torch



def tensor_creation():
    print("Tensor Creation:")
    a = torch.tensor([[1, 2, 3],
                    [4, 5, 6]],
                    dtype=torch.int32
    )
    print(a)

def tensor_shape_and_dimensions():
    print("Tensor Shape and Dimensions:")
    a = torch.tensor([[1, 2, 3],
                    [4, 5, 6]],
                    dtype=torch.int32
    )
    print("Shape:", a.shape)
    print("Dimensions:", a.ndim)

def tensor_data_types():
    print("Tensor Data Types:")
    a = torch.tensor([[1, 2, 3],
                    [4, 5, 6]],
                    dtype=torch.int32
    )
    print("Data Type:", a.dtype)

def tensor_element_access():
    print("Tensor Element Access:")
    a = torch.tensor([[1, 2, 3],
                    [4, 5, 6]],
                    dtype=torch.int32
    )
    print("Element at (0, 1):", a[0, 1])
    print("First row:", a[0])
    print("Second column:", a[:, 1])

def tensor_conversion(): # Chuyển đổi tensor sang numpy array 
    print("Tensor Conversion:")
    a = torch.tensor([[1, 2, 3],
                    [4, 5, 6]],
                    dtype=torch.int32
    )
    b = a.numpy()
    print("NumPy Array:\n", b)
    # CChuyển đổi NumPy array sang tensor
    c = torch.from_numpy(b)
    print("Tensor from NumPy Array:\n", c)

def tensor_device_management():
    print("Tensor Device Management:")
    a = torch.tensor([[1, 2, 3],
                    [4, 5, 6]],
                    dtype=torch.int32
    )
    print("Device:", a.device)

if __name__ == "__main__":
    tensor_creation()
    tensor_shape_and_dimensions()
    tensor_data_types()
    tensor_element_access()
    tensor_conversion()
    tensor_device_management()