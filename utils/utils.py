import torch
import random
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from torchsummary import summary 

class Utils:
    def __init__(self):
        pass

    def get_device(self):
        return 'cuda' if torch.cuda.is_available() else 'cpu'

    def show_random_images_for_each_class(self, train_data, num_images_per_class=16):
        for c, cls in enumerate(train_data.classes):
            rand_targets = random.sample([
                n
                for n, x in enumerate(train_data.targets)
                if x==c
            ], k=num_images_per_class)
            show_img_grid(
                np.transpose(train_data.data[rand_targets], axes=(0, 3, 1, 2))
            )
            plt.title(cls)
    

    def show_img_grid(self, data):
        try:
            grid_img = torchvision.utils.make_grid(data.cpu().detach())
        except:
            data = torch.from_numpy(data)
            grid_img = torchvision.utils.make_grid(data)
        
        plt.figure(figsize=(10, 10))
        plt.imshow(grid_img.permute(1, 2, 0))
        

    def show_random_images(self, data_loader):
        data, target  = next(iter(data_loader))
        self.show_img_grid(data)


    def show_model_summary(self, model, input_size=(1, 28, 28)):
        summary(model, input_size=input_size)
