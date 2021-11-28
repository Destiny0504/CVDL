from math import pi
import cv2
import numpy as np


def resize():
    pic = cv2.imread('./Q4_image/SQUARE-01.png')

    resized_pic = cv2.resize(pic,(256, 256), interpolation=False)
    cv2.imshow('resize', resized_pic)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def translation():
    pic = cv2.imread('./Q4_image/SQUARE-01.png')

    resized_pic = cv2.resize(pic,(256, 256), interpolation=False)
    translate_matrix = np.float32([[1, 0, 0], [0, 1, 60]])
    translated = cv2.warpAffine(resized_pic, translate_matrix, (pic.shape[1], pic.shape[0]))

    cv2.imshow('translate', translated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def scaling():
    pic = cv2.imread('./Q4_image/SQUARE-01.png')

    resized_pic = cv2.resize(pic,(256, 256), interpolation=False)

    translate_matrix = np.float32([[1, 0, 0], [0, 1, 60]])
    translated = cv2.warpAffine(resized_pic, translate_matrix, (pic.shape[1], pic.shape[0]))


    rotate = cv2.getRotationMatrix2D((128, 188), 10, 0.5)
    rotated = cv2.warpAffine(translated, rotate, (pic.shape[1], pic.shape[0]))

    cv2.imshow('rotate', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sharing():
    pic = cv2.imread('./Q4_image/SQUARE-01.png')

    resized_pic = cv2.resize(pic,(256, 256), interpolation=False)

    translate_matrix = np.float32([[1, 0, 0], [0, 1, 60]])
    translated = cv2.warpAffine(resized_pic, translate_matrix, (pic.shape[1], pic.shape[0]))

    rotate = cv2.getRotationMatrix2D((128, 188), 10, 0.5)
    rotated = cv2.warpAffine(translated, rotate, (pic.shape[1], pic.shape[0]))
    
    origin = np.float32([[50,50],[200,50],[50,200]])
    sharing = np.float32([[10,100],[200,50],[100,250]])

    sharing_matrix = cv2.getAffineTransform(origin,sharing)
    
    shared = cv2.warpAffine(rotated, sharing_matrix, (pic.shape[1], pic.shape[0]))
    cv2.imshow('sharing', shared)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    resize()
    translation()
    scaling()
    sharing()