import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from torchvision import models
import numpy as np
from matplotlib.pyplot import MultipleLocator

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

batch_size = 64
lr = 1e-4
optimizer = 'Adam'

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=2)

classes = [1,2,3,4,5,6,7,8,9,10]

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

def infer(which = 10):

    Model = models.vgg16()
    fine_tune = torch.nn.Linear(1000, 10)
    Model.eval()
    fine_tune.eval()
    print('start loading')
    Model.load_state_dict(torch.load('./vgg.model'))
    fine_tune.load_state_dict(torch.load('./finetune.model'))
    print('finish loading')
    testiter = iter(testloader)
    itr = 0
    for images, labels in testiter:
        if itr == which:
            break
        else:
            itr += 1
    outputs = Model(images)
    outputs = fine_tune(outputs)
    softmax = torch.nn.Softmax()
    output = softmax(outputs[0])
    output = output.detach().numpy()
    print(output)
    npimg = images[0].numpy()
    fig, axs = plt.subplots(1, 2)
    plt.subplot(1, 2, 1)
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.subplot(1, 2, 2)
    plt.bar(classes, output)
    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(0.1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.xlim(-0.5,10)
    plt.ylim(0.0,1)
    plt.show()
if __name__ =='__main__':
    print_func()

    