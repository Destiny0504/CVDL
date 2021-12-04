import cv2
import os
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size

def imgshow(title, pic):
    cv2.imshow(title, pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def create_Gaussian(s, sigma):

    s_mid = (s[0] - 1) // 2
    f = np.zeros(s)
    total = 0.0
    
    # calculate the Gaussian Filter
    for y in range(-s_mid, s_mid + 1):
        for x in range(-s_mid, s_mid + 1):
            f[y + s_mid][x + s_mid] = math.exp((-(y ** 2 + x ** 2)) ) / (2.0 * math.pi * (sigma ** 2))
            total += f[y + s_mid][x + s_mid]

    for y in range(len(f)):
        for x in range(len(f[y])):
            f[y][x] = f[y][x] / total

    return f


def conv2d(img, filter, stride=1):
    row, col = img.shape[0], img.shape[1]
    ft_mid = (filter.shape[0] - 1) // 2
    pad_img = np.pad(array = img, pad_width = ((ft_mid, ft_mid),(ft_mid, ft_mid)), mode='constant', constant_values=0)
    result = np.zeros((row, col))
    for r in range(ft_mid, row + ft_mid, stride):
        for c in range(ft_mid, col + ft_mid, stride):
            result[r - ft_mid][c - ft_mid] = np.sum(pad_img[r - ft_mid:r + ft_mid + 1, c - ft_mid:c + ft_mid + 1] * filter)

    return result


def Gaussian_blur():
    # file_path = os.path.join('Dataset_opencvdl', 'Q3_Image', 'Chihiro.jpg')
    pic = cv2.imread('./Q3_Image/House.jpg')
    imgshow('original', pic)
    filter = create_Gaussian((3, 3), 1.5)
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    imgshow('RGB to gray', gray)

    result = conv2d(gray, filter)
    result = result.astype('uint8')
    imgshow('Gaussian blur', result)
    return result

def Sobel_x(show = True):
    # file_path = os.path.join('Dataset_opencvdl', 'Q3_Image', 'Chihiro.jpg')
    pic = cv2.imread('./Q3_Image/House.jpg')
    gaussian_filter = create_Gaussian((3, 3), 1.5)
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    result = conv2d(gray, gaussian_filter)
    sobelx_filter = np.array(
        [
            [-1.0, 0.0, 1.0],
            [-2.0, 0.0, 2.0],
            [-1.0, 0.0, 1.0]
        ]
    )
    sobelx_result = conv2d(result, sobelx_filter)
    sobelx_result = np.abs(sobelx_result)
    if show:
        imgshow('sobelx_result', sobelx_result/255)
    return sobelx_result/255

def Sobel_y(show = True):
    # file_path = os.path.join('Dataset_opencvdl', 'Q3_Image', 'Chihiro.jpg')
    pic = cv2.imread('./Q3_Image/House.jpg')
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    gaussian_filter = create_Gaussian((3, 3), 1.5)
    g_result = conv2d(gray, gaussian_filter)

    sobely_filter = np.array(
        [
            [1.0, 2.0, 1.0],
            [0.0, 0.0, 0.0],
            [-1.0, -2.0, -1.0]
        ]
    )
    sobely_result = conv2d(g_result, sobely_filter)
    sobely_result = np.abs(sobely_result)
    if show:
        imgshow('sobely_result', sobely_result/255)
    return sobely_result/255

def Magnitude():
    img1 = Sobel_x(show=False)
    img2 = Sobel_y(show=False)
    mag = img1 ** 2 + img2 ** 2
    mag = mag ** 0.5

    return mag

if __name__ == "__main__":
    Gaussian_blur()
    print('finish Gaussian blur')
    img = Magnitude()
    print(img)
    imgshow('Magnitude', img)
