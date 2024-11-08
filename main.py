import torch

if __name__ == '__main__':

    x = torch.cuda.is_available()
    print(x)
