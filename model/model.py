import torch
import torch.nn as nn
import torch.nn.functional as F

dropout_value = 0.1

class Model(nn.Module):
    def __init__(self,
        in_channels, out_channels,
        k=3, s=1, p=1, 
        dilation=1, groups=1, bias=False,
        dropout_value=dropout_value,
        regularizers=True):
        super().__init__()
        layers = []
        layers.extend([
            nn.Conv2d(
                in_channels, out_channels, 
                k, s, p, 
                dilation, groups, bias,
            )
        ])
        if regularizers:
            layers.extend([
                nn.BatchNorm2d(out_channels),
                nn.ReLU(),
                nn.Dropout(dropout_value),
            ])
        self.custom_conv = nn.Sequential(*layers)
    
    def forward(self, x):
        x = self.custom_conv(x)
        return x


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        
        # C1 BLOCK
        self.convblock_0 = Model(3, 16)
        self.convblock_1 = Model(16, 32)
        self.convblock_2 = Model(32, 32)
        self.dilated_conv_1 = Model(32, 32, k=3, s=2, dilation=2)
        
        # C2 BLOCK
        self.convblock_3 = Model(32, 32)
        self.convblock_4 = Model(32, 52)
        self.dilated_conv_2 = Model(52, 64, k=3, s=2, dilation=2)
        
        # C3 BLOCK
        self.sep_conv_1 = Model(64, 64)
        self.convblock_7 = Model(64, 64)
        self.strided_conv_1 = Model(64, 64, k=1, s=2)
        
        # C4 BLOCK
        self.convblock_5 = Model(64, 64)
        self.convblock_6 = Model(64, 10, regularizers=False)
        
        # OUTPUT BLOCK
        self.gap = nn.AvgPool2d(kernel_size=5)
    
    def forward(self, x):

        # C1 BLOCK
        x = self.convblock_0(x)
        x = self.convblock_1(x)
        x = self.convblock_2(x)
        x = self.dilated_conv_1(x)

        # C2 BLOCK      

        x = self.convblock_3(x)
        x = self.convblock_4(x)
        x = self.dilated_conv_2(x)


        # C3 BLOCK
        x = self.sep_conv_1(x)
        x = self.convblock_7(x)
        x = self.strided_conv_1(x)
        # C4 BLOCK
        x = self.convblock_5(x)
        x = self.convblock_6(x)

        # OUTPUT BLOCK

        x = self.gap(x)
        
        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)
