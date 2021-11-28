import cv2
import os
import numpy as np

# pic = cv2.imread('./Q1_image/Sun.jpg')
# cv2.imshow('sun',pic)
# height, width, channels = pic.shape

# print(height)
# print(width)
# print(channels)

def loadimage():
    # file_path = os.path.join('Dataset_OpenCvDl_Hw1', 'Q1_Image', 'Sun.jpg')
    # print(f'\nfile_path : {file_path}')
    pic = cv2.imread('./Q1_Image/Sun.jpg')
    print('Height = ', pic.shape[0])
    print('Width = ', pic.shape[1])
    cv2.startWindowThread()
    cv2.imshow('Sun', pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def colorSep():
    # file_path = os.path.join('Dataset_OpenCvDl_Hw1', 'Q1_Image', 'Sun.jpg')
    # print(file_path)
    pic = cv2.imread('./Q1_Image/Sun.jpg')
    
    B, G, R = cv2.split(pic)

    zeros = np.zeros(pic.shape[:2], dtype = 'uint8')

    cv2.imshow('B', cv2.merge([B, zeros, zeros]))
    cv2.imshow('G', cv2.merge([zeros, G, zeros]))
    cv2.imshow('R', cv2.merge([zeros, zeros, R]))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def color_transform():
    pic = cv2.imread('./Q1_Image/Sun.jpg')
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    cv2.imshow('OpenCV function', gray)

    B, G, R = cv2.split(pic)

    cv2.imshow('Averaged function', (B + G + R) // 3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

def Blending():
    pic_weak = cv2.imread('./Q1_Image/Dog_Weak.jpg')
    pic_strong = cv2.imread('./Q1_Image/Dog_Strong.jpg')

    def do_nothing(x):
        pass
    cv2.namedWindow('Blending')
    cv2.createTrackbar('TB', 'Blending', 0, 100, do_nothing)

    while True:
        alpha = cv2.getTrackbarPos('TB', 'Blending')
        beta = (1.0 - alpha / 100)
        dst = cv2.addWeighted(pic_strong, alpha/100, pic_weak, beta, 0)
        cv2.imshow('Blending', dst)
        k = cv2.waitKey(1)
        if k != -1:
            break

    pass
if __name__ == "__main__":
    color_transform()
# cv2.waitKey(0)