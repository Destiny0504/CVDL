from math import pi
import cv2
import numpy as np

def transform(rotate=10, scale=0.5, tx=0, ty=60):
    # file_path = os.path.join('Dataset_opencvdl', 'Q4_Image', 'Parrot.png')
    pic = cv2.imread('./Q4_image/SQUARE-01.png')
    cv2.imshow('do nothing', pic)

    resized_pic = cv2.resize(pic,(256, 256), interpolation=False)
    cv2.imshow('resize', resized_pic)

    cv2.namedWindow("transform", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("transform", 400, 300)

    cv2.namedWindow("rotate", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("rotate", 400, 300)

    # cv2.namedWindow("sharing", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("sharing", 400, 300)

    translate_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated = cv2.warpAffine(resized_pic, translate_matrix, (pic.shape[1], pic.shape[0]))

    cv2.imshow('transform', translated)

    rotate = cv2.getRotationMatrix2D((128, 188), rotate, scale)
    rotated = cv2.warpAffine(translated, rotate, (pic.shape[1], pic.shape[0]))

    cv2.imshow('rotate', rotated)

    sharing_matrix

    #cv2.imshow('transform',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    transform()