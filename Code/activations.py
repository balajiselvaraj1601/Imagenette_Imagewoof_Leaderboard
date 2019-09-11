#############################################################################

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.nn.parameter import Parameter

############################## Implementations ############################## 

class Msh(nn.Module):	
	def __init__(self):
		super(Msh, self).__init__()
	def forward(self, x):
		y = x * (torch.tanh(F.softplus(x)))
		return y

"""
class Mish(nn.Module):
    def __init__(self):
        super().__init__()
        print("Mish activation loaded...")

    def forward(self, x):  
        #save 1 second per epoch with no x= x*() and then return x...just inline it.
        return x *( torch.tanh(F.softplus(x))) 
"""

# Code for new_activation is not shared

functions=dict({ 'msh'				:"Msh()"							, 		
		'new_activ'			:"new_activation()"				,	
		})

