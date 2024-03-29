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
![image](https://github.com/ShubhamVerma16/ERA-Session-9/assets/46774613/f2608d0b-bc50-4390-a00e-2b2fb54ba461)
