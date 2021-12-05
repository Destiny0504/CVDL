from torchvision import models
import torch
import torchvision
import torchvision.transforms as transforms
import copy
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from tqdm import tqdm

torch.manual_seed(14)
torch.cuda.manual_seed(14)
np.random.seed(14)
random.seed(14)
torch.backends.cudnn.deterministic = True
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

Model = models.vgg16(pretrained=True)
linear = torch.nn.Linear(1000, 10)

batch_size = 64
LR = 1e-4
optimizer = torch.optim.Adam(Model.parameters(), lr=LR)

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

def train_model(model, finetune, dataloaders, criterion, optimizer, num_epochs=25, is_inception=False):
    val_acc_history = []
    loss_history = []
    best_model_wts = copy.deepcopy(model.state_dict())
    best_finetune_model = copy.deepcopy(finetune.state_dict())
    best_acc = 0.0

    for epoch in tqdm(range(num_epochs)):
        print('Epoch {}/{}'.format(epoch + 1, num_epochs))
        print('-' * 30)

        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()   # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for inputs, labels in iter(dataloaders[phase]):
                inputs = inputs.to('cuda:0')
                labels = labels.to('cuda:0')
                model = model.to('cuda:0')
                finetune = finetune.to('cuda:0')
                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    # Get model outputs and calculate loss
                    # Special case for inception because in training it has an auxiliary output. In train
                    #   mode we calculate the loss by summing the final output and the auxiliary output
                    #   but in testing we only consider the final output.
                    if is_inception and phase == 'train':
                        # From https://discuss.pytorch.org/t/how-to-optimize-inception-model-with-auxiliary-classifiers/7958
                        outputs, aux_outputs = model(inputs)
                        loss1 = criterion(outputs, labels)
                        loss2 = criterion(aux_outputs, labels)
                        loss = loss1 + 0.4*loss2
                    else:
                        outputs = model(inputs)
                        outputs = finetune(outputs)
                        # print(len(outputs))
                        # print(len(outputs[0]))
                        loss = criterion(outputs, labels)

                    _, preds = torch.max(outputs, 1)
                    # print(preds)
                    # print(labels.data)
                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()
                        #print('propagation')

                # statistics
                running_loss += loss.item() * inputs.size(0)
                # print(labels.data)
                running_corrects += torch.sum(preds == labels.data)
            # print(len(dataloaders[phase].dataset))
            epoch_loss = running_loss / len(dataloaders[phase].dataset)
            epoch_acc = running_corrects.double() / len(dataloaders[phase].dataset)
            if phase == 'train':
                loss_history.append(epoch_loss)
            print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))
            # deep copy the model
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())
                best_finetune_model = copy.deepcopy(finetune.state_dict())
            if phase == 'val':
                epoch_acc.to('cpu')
                val_acc = copy.deepcopy(epoch_acc)
                val_acc_history.append(val_acc)
                epoch_acc.to('cuda:0')
                
        print()
    print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    finetune.load_state_dict(best_finetune_model)
    return model, val_acc_history, finetune, optimizer,loss_history

if __name__ =='__main__':
    torch.manual_seed(14)
    # test_save = torch.nn.Linear(10,10)
    # torch.save(test_save.state_dict(), './test_save.model')
    # test_model = torch.nn.Linear(10,10)
    # test_model.load_state_dict(torch.load('./test_save.model'))
    # test_model.eval()
    # test = torch.ones(10)
    # output = test_model(test)
    # print(output)
    epoches = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    training_history = [0.8364,0.8375,0.8616,0.8684,0.8689,0.8686,0.8709,0.8751,0.8693,0.8754,0.8711,0.8761,0.8736,0.8809,0.8752,0.8645,0.8833,0.8726,0.8742,0.8788]
    loss = [0.7087398716926575,0.38122967779159544,0.23286657293558122,0.16360180432915689,0.11836221212029457,
    0.10069130469530821,0.08638890918016434,0.0641276462251693,0.06587327937748283,0.06266105379194022,
    0.05688207668669522,0.05086910744357854,0.047305624182866886,0.04502988857470453,0.04207388549212367,
    0.04452099914579652,0.0423911630965909,0.03786786889869254,0.03569341274626553,0.038413986393268276]
    # vgg16_model, training_history, finetune_model, cur_optimizer, loss = train_model(Model, linear
    # , dataloaders={'train':trainloader,'val':testloader},criterion=torch.nn.CrossEntropyLoss(),optimizer=optimizer,num_epochs=20)
    # vgg16_model = vgg16_model.to('cpu')
    # finetune_model = finetune_model.to('cpu')
    # print(training_history)
    # print(loss)
    # torch.save(vgg16_model.state_dict(), './vgg.model')
    # torch.save(finetune_model.state_dict(), './finetune.model')
    # torch.save(cur_optimizer.state_dict(), './vgg_optimizer')
    plt.figure(figsize=(15,10),dpi=100,linewidth = 1)
    plt.plot(epoches, training_history,'o-',color = 'r', label="Accuracy")
    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(0.02)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.xlim(-0.5,20)
    plt.ylim(0.8,1)
    plt.savefig('fig1.png')
    plt.show()
    plt.figure(figsize=(15,10),dpi=100,linewidth = 1)
    plt.plot(epoches, loss,'s-',color = 'r', label="Accuracy")
    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(0.5)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.xlim(-0.5,20)
    plt.ylim(-0.1,1)
    plt.savefig('fig2.png')
    plt.show()
