import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np


transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

batch_size = 16
lr = 1e-3
optimizer = 'Adam'

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

def load_data():
    dataiter = iter(trainloader)
    images, labels = dataiter.next()
    print(int(labels[0]))
    class_for_load = list(classes)
    print(class_for_load)
    torchvision.utils.make_grid(images[:10])
    fig, axs = plt.subplots(3, 3)
    for i in range(1,10):
        img = images[i]
        img = img / 2 + 0.5     # unnormalize
        npimg = img.numpy()
        plt.subplot(3, 3, i)
        plt.axis('off')
        plt.title(class_for_load[int(labels[i])])
        np.transpose(npimg, (1, 2, 0))
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

def print_hyper():
    print('hyperparameters:')
    print(f'batch_size : {batch_size}')
    print(f'learning rate : {lr}')
    print(f'optimizer : {optimizer}')

def print_func():
    from torchvision import models
    Model = models.vgg16() 
    print(Model)

if __name__ =='__main__':
    #load_data()
    print_func()

    