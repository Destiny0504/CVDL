import cv2
import os

def Gaussian():
    # file_path = os.path.join('Dataset_opencvdl', 'Q2_Image', 'Cat.png')
    pic = cv2.imread('./Q2_Image/Lenna_whiteNoise.jpg')
    result = cv2.GaussianBlur(pic, (5, 5), 1.5)

    cv2.imshow('Gaussian', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Bilateral():
    # file_path = os.path.join('Dataset_opencvdl', 'Q2_Image', 'Cat.png')
    pic = cv2.imread('./Q2_Image/Lenna_whiteNoise.jpg')
    result = cv2.bilateralFilter(pic, 9, 90, 90)

    cv2.imshow('Bilateral', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def median():
    # file_path = os.path.join('Dataset_opencvdl', 'Q2_Image', 'Cat.png')
    pic = cv2.imread('./Q2_Image/Lenna_pepperSalt.jpg')
    mb3 = cv2.medianBlur(pic, 3)
    mb5 = cv2.medianBlur(pic, 5)

    cv2.imshow('median3', mb3)
    cv2.imshow('median5', mb5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    median()