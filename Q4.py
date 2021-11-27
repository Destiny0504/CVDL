import cv2
import os
import numpy as np

def transform(rot=30, scale=0.9, tx=200, ty=300):
    # file_path = os.path.join('Dataset_opencvdl', 'Q4_Image', 'Parrot.png')
    pic = cv2.imread('./Q4_image/SQUARE-01.png')

    M = cv2.getRotationMatrix2D((160, 84), rot, scale)
    M[0, 2] += ty
    M[1, 2] += tx
    res = cv2.warpAffine(pic, M, (pic.shape[1], pic.shape[0]))


    cv2.imshow('transform', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    transform()