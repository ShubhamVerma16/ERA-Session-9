# ERA-Session-9

## Session Target
* [x] Write a new network that has the architecture to C1C2C3C40 (No MaxPooling, but 3 convolutions, where the last one has a stride of 2 instead) (If you can figure out how to use Dilated kernels here instead of MP or strided convolution, then 200pts extra!)
* [x] total RF must be more than 44
* [x] one of the layers must use Depthwise Separable Convolution
* [x] one of the layers must use Dilated Convolution
* [x] use GAP (compulsory):- add FC after GAP to target #of classes (optional)
* [x] use albumentation library and apply: horizontal flip shiftScaleRotate coarseDropout (max_holes = 1, max_height=16px, max_width=16, min_holes = 1, min_height=16px, min_width=16px, fill_value=(mean of your dataset), mask_fill_value = None)
* [x] achieve 85% accuracy, as many epochs as you want. Total Params to be less than 200k.
* [x] make sure you're following code-modularity (else 0 for full assignment)
* [x] upload to Github

## CIFAR10 Images
![image](https://github.com/ShubhamVerma16/ERA-Session-9/assets/46774613/e65faa85-62c8-4846-89fc-fcc539ae02db)

## Model Summary
```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 16, 32, 32]             432
       BatchNorm2d-2           [-1, 16, 32, 32]              32
              ReLU-3           [-1, 16, 32, 32]               0
           Dropout-4           [-1, 16, 32, 32]               0
             Model-5           [-1, 16, 32, 32]               0
            Conv2d-6           [-1, 32, 32, 32]           4,608
       BatchNorm2d-7           [-1, 32, 32, 32]              64
              ReLU-8           [-1, 32, 32, 32]               0
           Dropout-9           [-1, 32, 32, 32]               0
            Model-10           [-1, 32, 32, 32]               0
           Conv2d-11           [-1, 32, 32, 32]           9,216
      BatchNorm2d-12           [-1, 32, 32, 32]              64
             ReLU-13           [-1, 32, 32, 32]               0
          Dropout-14           [-1, 32, 32, 32]               0
            Model-15           [-1, 32, 32, 32]               0
           Conv2d-16           [-1, 32, 15, 15]           9,216
      BatchNorm2d-17           [-1, 32, 15, 15]              64
             ReLU-18           [-1, 32, 15, 15]               0
          Dropout-19           [-1, 32, 15, 15]               0
            Model-20           [-1, 32, 15, 15]               0
           Conv2d-21           [-1, 32, 15, 15]           9,216
      BatchNorm2d-22           [-1, 32, 15, 15]              64
             ReLU-23           [-1, 32, 15, 15]               0
          Dropout-24           [-1, 32, 15, 15]               0
            Model-25           [-1, 32, 15, 15]               0
           Conv2d-26           [-1, 52, 15, 15]          14,976
      BatchNorm2d-27           [-1, 52, 15, 15]             104
             ReLU-28           [-1, 52, 15, 15]               0
          Dropout-29           [-1, 52, 15, 15]               0
            Model-30           [-1, 52, 15, 15]               0
           Conv2d-31             [-1, 64, 7, 7]          29,952
      BatchNorm2d-32             [-1, 64, 7, 7]             128
             ReLU-33             [-1, 64, 7, 7]               0
          Dropout-34             [-1, 64, 7, 7]               0
            Model-35             [-1, 64, 7, 7]               0
           Conv2d-36             [-1, 64, 7, 7]          36,864
      BatchNorm2d-37             [-1, 64, 7, 7]             128
             ReLU-38             [-1, 64, 7, 7]               0
          Dropout-39             [-1, 64, 7, 7]               0
            Model-40             [-1, 64, 7, 7]               0
           Conv2d-41             [-1, 64, 7, 7]          36,864
      BatchNorm2d-42             [-1, 64, 7, 7]             128
             ReLU-43             [-1, 64, 7, 7]               0
          Dropout-44             [-1, 64, 7, 7]               0
            Model-45             [-1, 64, 7, 7]               0
           Conv2d-46             [-1, 64, 5, 5]           4,096
      BatchNorm2d-47             [-1, 64, 5, 5]             128
             ReLU-48             [-1, 64, 5, 5]               0
          Dropout-49             [-1, 64, 5, 5]               0
            Model-50             [-1, 64, 5, 5]               0
           Conv2d-51             [-1, 64, 5, 5]          36,864
      BatchNorm2d-52             [-1, 64, 5, 5]             128
             ReLU-53             [-1, 64, 5, 5]               0
          Dropout-54             [-1, 64, 5, 5]               0
            Model-55             [-1, 64, 5, 5]               0
           Conv2d-56             [-1, 10, 5, 5]           5,760
            Model-57             [-1, 10, 5, 5]               0
        AvgPool2d-58             [-1, 10, 1, 1]               0
================================================================
Total params: 199,096
Trainable params: 199,096
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.01
Forward/backward pass size (MB): 4.61
Params size (MB): 0.76
Estimated Total Size (MB): 5.38
----------------------------------------------------------------
```
## Training Logs
```
[EPOCH 0 / 300]
Loss=1.5191657543182373 Batch_id=390 Accuracy=30.57: 100%|██████████| 391/391 [00:23<00:00, 16.92it/s]

Test set: Average loss: 1.5925, Accuracy: 4200/10000 (42.00%)

[EPOCH 1 / 300]
Loss=1.493445873260498 Batch_id=390 Accuracy=44.42: 100%|██████████| 391/391 [00:20<00:00, 18.71it/s]

Test set: Average loss: 1.3615, Accuracy: 5101/10000 (51.01%)

[EPOCH 2 / 300]
Loss=1.2844377756118774 Batch_id=390 Accuracy=49.87: 100%|██████████| 391/391 [00:21<00:00, 18.28it/s]

Test set: Average loss: 1.2401, Accuracy: 5650/10000 (56.50%)

[EPOCH 3 / 300]
Loss=1.1438052654266357 Batch_id=390 Accuracy=54.44: 100%|██████████| 391/391 [00:21<00:00, 18.38it/s]

Test set: Average loss: 1.0451, Accuracy: 6241/10000 (62.41%)

[EPOCH 4 / 300]
Loss=0.9190350770950317 Batch_id=390 Accuracy=57.99: 100%|██████████| 391/391 [00:21<00:00, 18.41it/s]

Test set: Average loss: 0.9424, Accuracy: 6639/10000 (66.39%)

[EPOCH 5 / 300]
Loss=1.0419518947601318 Batch_id=390 Accuracy=60.93: 100%|██████████| 391/391 [00:20<00:00, 19.31it/s]

Test set: Average loss: 0.8516, Accuracy: 6982/10000 (69.82%)

[EPOCH 6 / 300]
Loss=1.075282335281372 Batch_id=390 Accuracy=62.34: 100%|██████████| 391/391 [00:20<00:00, 18.84it/s]

Test set: Average loss: 0.7970, Accuracy: 7162/10000 (71.62%)

[EPOCH 7 / 300]
Loss=1.0363472700119019 Batch_id=390 Accuracy=63.91: 100%|██████████| 391/391 [00:21<00:00, 18.42it/s]

Test set: Average loss: 0.7437, Accuracy: 7375/10000 (73.75%)

[EPOCH 8 / 300]
Loss=1.0084865093231201 Batch_id=390 Accuracy=64.68: 100%|██████████| 391/391 [00:22<00:00, 17.40it/s]

Test set: Average loss: 0.7483, Accuracy: 7387/10000 (73.87%)

[EPOCH 9 / 300]
Loss=1.135936975479126 Batch_id=390 Accuracy=66.32: 100%|██████████| 391/391 [00:20<00:00, 19.21it/s]

Test set: Average loss: 0.6792, Accuracy: 7609/10000 (76.09%)

[EPOCH 10 / 300]
Loss=1.1049538850784302 Batch_id=390 Accuracy=67.21: 100%|██████████| 391/391 [00:20<00:00, 18.76it/s]

Test set: Average loss: 0.6423, Accuracy: 7757/10000 (77.57%)

[EPOCH 11 / 300]
Loss=0.9754637479782104 Batch_id=390 Accuracy=67.79: 100%|██████████| 391/391 [00:21<00:00, 18.39it/s]

Test set: Average loss: 0.6322, Accuracy: 7821/10000 (78.21%)

[EPOCH 12 / 300]
Loss=0.8267175555229187 Batch_id=390 Accuracy=68.48: 100%|██████████| 391/391 [00:21<00:00, 18.30it/s]

Test set: Average loss: 0.6275, Accuracy: 7832/10000 (78.32%)

[EPOCH 13 / 300]
Loss=1.0994455814361572 Batch_id=390 Accuracy=68.99: 100%|██████████| 391/391 [00:20<00:00, 19.26it/s]

Test set: Average loss: 0.6156, Accuracy: 7855/10000 (78.55%)

[EPOCH 14 / 300]
Loss=0.8465280532836914 Batch_id=390 Accuracy=69.53: 100%|██████████| 391/391 [00:21<00:00, 18.46it/s]

Test set: Average loss: 0.5929, Accuracy: 7974/10000 (79.74%)

[EPOCH 15 / 300]
Loss=0.9766108393669128 Batch_id=390 Accuracy=69.96: 100%|██████████| 391/391 [00:21<00:00, 17.97it/s]

Test set: Average loss: 0.6370, Accuracy: 7752/10000 (77.52%)

[EPOCH 16 / 300]
Loss=0.8733251690864563 Batch_id=390 Accuracy=70.24: 100%|██████████| 391/391 [00:22<00:00, 17.61it/s]

Test set: Average loss: 0.5680, Accuracy: 8017/10000 (80.17%)

[EPOCH 17 / 300]
Loss=0.8712032437324524 Batch_id=390 Accuracy=70.67: 100%|██████████| 391/391 [00:20<00:00, 19.14it/s]

Test set: Average loss: 0.5473, Accuracy: 8089/10000 (80.89%)

[EPOCH 18 / 300]
Loss=0.7678402662277222 Batch_id=390 Accuracy=71.22: 100%|██████████| 391/391 [00:20<00:00, 19.14it/s]

Test set: Average loss: 0.5572, Accuracy: 8085/10000 (80.85%)

[EPOCH 19 / 300]
Loss=0.6793580651283264 Batch_id=390 Accuracy=71.64: 100%|██████████| 391/391 [00:21<00:00, 18.59it/s]

Test set: Average loss: 0.5362, Accuracy: 8152/10000 (81.52%)

[EPOCH 20 / 300]
Loss=0.8212993741035461 Batch_id=390 Accuracy=71.76: 100%|██████████| 391/391 [00:21<00:00, 18.46it/s]

Test set: Average loss: 0.5558, Accuracy: 8056/10000 (80.56%)

[EPOCH 21 / 300]
Loss=0.7572979927062988 Batch_id=390 Accuracy=72.14: 100%|██████████| 391/391 [00:20<00:00, 19.03it/s]

Test set: Average loss: 0.5296, Accuracy: 8187/10000 (81.87%)

[EPOCH 22 / 300]
Loss=0.7302656173706055 Batch_id=390 Accuracy=72.15: 100%|██████████| 391/391 [00:20<00:00, 19.09it/s]

Test set: Average loss: 0.5400, Accuracy: 8084/10000 (80.84%)

[EPOCH 23 / 300]
Loss=0.6675785779953003 Batch_id=390 Accuracy=72.35: 100%|██████████| 391/391 [00:21<00:00, 18.27it/s]

Test set: Average loss: 0.5148, Accuracy: 8234/10000 (82.34%)

[EPOCH 24 / 300]
Loss=0.7922696471214294 Batch_id=390 Accuracy=72.81: 100%|██████████| 391/391 [00:24<00:00, 16.14it/s]

Test set: Average loss: 0.5093, Accuracy: 8214/10000 (82.14%)

[EPOCH 25 / 300]
Loss=0.7900272607803345 Batch_id=390 Accuracy=73.01: 100%|██████████| 391/391 [00:23<00:00, 16.56it/s]

Test set: Average loss: 0.4906, Accuracy: 8298/10000 (82.98%)

[EPOCH 26 / 300]
Loss=0.7619772553443909 Batch_id=390 Accuracy=72.97: 100%|██████████| 391/391 [00:20<00:00, 18.97it/s]

Test set: Average loss: 0.4925, Accuracy: 8310/10000 (83.10%)

[EPOCH 27 / 300]
Loss=0.9692867398262024 Batch_id=390 Accuracy=73.32: 100%|██████████| 391/391 [00:21<00:00, 18.50it/s]

Test set: Average loss: 0.4990, Accuracy: 8240/10000 (82.40%)

[EPOCH 28 / 300]
Loss=0.7864417433738708 Batch_id=390 Accuracy=73.61: 100%|██████████| 391/391 [00:21<00:00, 18.26it/s]

Test set: Average loss: 0.4939, Accuracy: 8286/10000 (82.86%)

[EPOCH 29 / 300]
Loss=0.7904437780380249 Batch_id=390 Accuracy=73.50: 100%|██████████| 391/391 [00:20<00:00, 18.71it/s]

Test set: Average loss: 0.4858, Accuracy: 8305/10000 (83.05%)

[EPOCH 30 / 300]
Loss=0.6308965086936951 Batch_id=390 Accuracy=73.68: 100%|██████████| 391/391 [00:20<00:00, 19.14it/s]

Test set: Average loss: 0.4818, Accuracy: 8364/10000 (83.64%)

[EPOCH 31 / 300]
Loss=0.6404911875724792 Batch_id=390 Accuracy=74.15: 100%|██████████| 391/391 [00:20<00:00, 18.76it/s]

Test set: Average loss: 0.4828, Accuracy: 8337/10000 (83.37%)

[EPOCH 32 / 300]
Loss=0.7255097031593323 Batch_id=390 Accuracy=74.17: 100%|██████████| 391/391 [00:22<00:00, 17.58it/s]

Test set: Average loss: 0.4767, Accuracy: 8349/10000 (83.49%)

[EPOCH 33 / 300]
Loss=0.6859000325202942 Batch_id=390 Accuracy=74.25: 100%|██████████| 391/391 [00:21<00:00, 18.32it/s]

Test set: Average loss: 0.4696, Accuracy: 8409/10000 (84.09%)

[EPOCH 34 / 300]
Loss=0.6726081967353821 Batch_id=390 Accuracy=74.32: 100%|██████████| 391/391 [00:20<00:00, 19.06it/s]

Test set: Average loss: 0.4670, Accuracy: 8382/10000 (83.82%)

[EPOCH 35 / 300]
Loss=0.8124157786369324 Batch_id=390 Accuracy=74.71: 100%|██████████| 391/391 [00:20<00:00, 19.27it/s]

Test set: Average loss: 0.4612, Accuracy: 8412/10000 (84.12%)

[EPOCH 36 / 300]
Loss=0.5937564373016357 Batch_id=390 Accuracy=74.89: 100%|██████████| 391/391 [00:21<00:00, 18.40it/s]

Test set: Average loss: 0.4776, Accuracy: 8363/10000 (83.63%)

[EPOCH 37 / 300]
Loss=0.7147809267044067 Batch_id=390 Accuracy=75.13: 100%|██████████| 391/391 [00:21<00:00, 18.12it/s]

Test set: Average loss: 0.4539, Accuracy: 8441/10000 (84.41%)

[EPOCH 38 / 300]
Loss=0.6928490400314331 Batch_id=390 Accuracy=74.93: 100%|██████████| 391/391 [00:20<00:00, 18.95it/s]

Test set: Average loss: 0.4531, Accuracy: 8458/10000 (84.58%)

[EPOCH 39 / 300]
Loss=0.7003346681594849 Batch_id=390 Accuracy=74.94: 100%|██████████| 391/391 [00:20<00:00, 19.15it/s]

Test set: Average loss: 0.4506, Accuracy: 8454/10000 (84.54%)

[EPOCH 40 / 300]
Loss=0.6248880624771118 Batch_id=390 Accuracy=74.97: 100%|██████████| 391/391 [00:21<00:00, 18.19it/s]

Test set: Average loss: 0.4460, Accuracy: 8461/10000 (84.61%)

[EPOCH 41 / 300]
Loss=0.9053980708122253 Batch_id=390 Accuracy=75.45: 100%|██████████| 391/391 [00:22<00:00, 17.36it/s]

Test set: Average loss: 0.4591, Accuracy: 8428/10000 (84.28%)

[EPOCH 42 / 300]
Loss=0.747511088848114 Batch_id=390 Accuracy=75.33: 100%|██████████| 391/391 [00:20<00:00, 18.77it/s]

Test set: Average loss: 0.4493, Accuracy: 8452/10000 (84.52%)

[EPOCH 43 / 300]
Loss=0.5464920401573181 Batch_id=390 Accuracy=75.48: 100%|██████████| 391/391 [00:20<00:00, 19.01it/s]

Test set: Average loss: 0.4491, Accuracy: 8475/10000 (84.75%)

[EPOCH 44 / 300]
Loss=0.6505069136619568 Batch_id=390 Accuracy=75.11: 100%|██████████| 391/391 [00:21<00:00, 18.21it/s]

Test set: Average loss: 0.4384, Accuracy: 8473/10000 (84.73%)

[EPOCH 45 / 300]
Loss=0.6888412237167358 Batch_id=390 Accuracy=75.86: 100%|██████████| 391/391 [00:21<00:00, 18.26it/s]

Test set: Average loss: 0.4309, Accuracy: 8492/10000 (84.92%)

[EPOCH 46 / 300]
Loss=0.7012165784835815 Batch_id=390 Accuracy=75.85: 100%|██████████| 391/391 [00:21<00:00, 18.36it/s]

Test set: Average loss: 0.4343, Accuracy: 8502/10000 (85.02%)

[EPOCH 47 / 300]
Loss=0.8552225232124329 Batch_id=390 Accuracy=76.05: 100%|██████████| 391/391 [00:20<00:00, 18.93it/s]

Test set: Average loss: 0.4414, Accuracy: 8474/10000 (84.74%)

[EPOCH 48 / 300]
Loss=0.733605682849884 Batch_id=390 Accuracy=75.98: 100%|██████████| 391/391 [00:20<00:00, 18.96it/s]

Test set: Average loss: 0.4373, Accuracy: 8506/10000 (85.06%)

[EPOCH 49 / 300]
Loss=0.6506266593933105 Batch_id=390 Accuracy=76.18: 100%|██████████| 391/391 [00:23<00:00, 16.94it/s]

Test set: Average loss: 0.4329, Accuracy: 8529/10000 (85.29%)

[EPOCH 50 / 300]
Loss=0.6419416069984436 Batch_id=390 Accuracy=77.34: 100%|██████████| 391/391 [00:21<00:00, 17.83it/s]

Test set: Average loss: 0.4033, Accuracy: 8635/10000 (86.35%)

[EPOCH 51 / 300]
Loss=0.4899563193321228 Batch_id=390 Accuracy=77.59: 100%|██████████| 391/391 [00:21<00:00, 17.99it/s]

Test set: Average loss: 0.4000, Accuracy: 8639/10000 (86.39%)

[EPOCH 52 / 300]
Loss=0.8522634506225586 Batch_id=390 Accuracy=77.62: 100%|██████████| 391/391 [00:21<00:00, 18.33it/s]

Test set: Average loss: 0.3957, Accuracy: 8647/10000 (86.47%)

[EPOCH 53 / 300]
Loss=0.7739626169204712 Batch_id=390 Accuracy=77.54: 100%|██████████| 391/391 [00:21<00:00, 18.53it/s]

Test set: Average loss: 0.3953, Accuracy: 8644/10000 (86.44%)

[EPOCH 54 / 300]
Loss=0.9148162603378296 Batch_id=390 Accuracy=77.83: 100%|██████████| 391/391 [00:22<00:00, 17.77it/s]

Test set: Average loss: 0.3962, Accuracy: 8666/10000 (86.66%)

[EPOCH 55 / 300]
Loss=0.7242871522903442 Batch_id=390 Accuracy=78.04: 100%|██████████| 391/391 [00:22<00:00, 17.70it/s]

Test set: Average loss: 0.3929, Accuracy: 8664/10000 (86.64%)

[EPOCH 56 / 300]
Loss=0.4842507243156433 Batch_id=390 Accuracy=78.01: 100%|██████████| 391/391 [00:21<00:00, 17.93it/s]

Test set: Average loss: 0.3907, Accuracy: 8678/10000 (86.78%)

[EPOCH 57 / 300]
Loss=0.6183480024337769 Batch_id=390 Accuracy=77.92: 100%|██████████| 391/391 [00:22<00:00, 17.58it/s]

Test set: Average loss: 0.3916, Accuracy: 8678/10000 (86.78%)

[EPOCH 58 / 300]
Loss=0.469734251499176 Batch_id=390 Accuracy=78.02: 100%|██████████| 391/391 [00:20<00:00, 18.71it/s]

Test set: Average loss: 0.3900, Accuracy: 8677/10000 (86.77%)

[EPOCH 59 / 300]
Loss=0.6399385333061218 Batch_id=390 Accuracy=78.31: 100%|██████████| 391/391 [00:22<00:00, 17.63it/s]

Test set: Average loss: 0.3902, Accuracy: 8685/10000 (86.85%)

[EPOCH 60 / 300]
Loss=0.4747212827205658 Batch_id=390 Accuracy=78.22: 100%|██████████| 391/391 [00:21<00:00, 17.82it/s]

Test set: Average loss: 0.3880, Accuracy: 8692/10000 (86.92%)

[EPOCH 61 / 300]
Loss=0.6261941194534302 Batch_id=390 Accuracy=78.40: 100%|██████████| 391/391 [00:21<00:00, 18.12it/s]

Test set: Average loss: 0.3856, Accuracy: 8691/10000 (86.91%)

[EPOCH 62 / 300]
Loss=0.5733634233474731 Batch_id=390 Accuracy=78.33: 100%|██████████| 391/391 [00:20<00:00, 19.01it/s]

Test set: Average loss: 0.3864, Accuracy: 8693/10000 (86.93%)

[EPOCH 63 / 300]
Loss=0.5571128726005554 Batch_id=390 Accuracy=78.38: 100%|██████████| 391/391 [00:21<00:00, 18.15it/s]

Test set: Average loss: 0.3852, Accuracy: 8684/10000 (86.84%)

[EPOCH 64 / 300]
Loss=0.602064847946167 Batch_id=390 Accuracy=78.31: 100%|██████████| 391/391 [00:21<00:00, 18.12it/s]

Test set: Average loss: 0.3873, Accuracy: 8698/10000 (86.98%)

[EPOCH 65 / 300]
Loss=0.38789018988609314 Batch_id=390 Accuracy=78.31: 100%|██████████| 391/391 [00:22<00:00, 17.14it/s]

Test set: Average loss: 0.3831, Accuracy: 8702/10000 (87.02%)

[EPOCH 66 / 300]
Loss=0.7895219922065735 Batch_id=390 Accuracy=78.50: 100%|██████████| 391/391 [00:21<00:00, 18.23it/s]

Test set: Average loss: 0.3837, Accuracy: 8713/10000 (87.13%)

[EPOCH 67 / 300]
Loss=0.8610292673110962 Batch_id=390 Accuracy=78.59: 100%|██████████| 391/391 [00:21<00:00, 18.41it/s]

Test set: Average loss: 0.3834, Accuracy: 8693/10000 (86.93%)

[EPOCH 68 / 300]
Loss=0.6174938678741455 Batch_id=390 Accuracy=78.44: 100%|██████████| 391/391 [00:21<00:00, 17.79it/s]

Test set: Average loss: 0.3832, Accuracy: 8710/10000 (87.10%)
```
