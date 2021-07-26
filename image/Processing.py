import cv2 as cv
import numpy as np


def PencilSketch(img:np.ndarray,isGray:bool = False) -> np.ndarray:
    dst_gray:np.ndarray;dst_color:np.ndarray
    #TODO: Gray and Color param need adjusment
    dst_gray, dst_color = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 
    if(isGray == True):
        return dst_gray
    else:
        return dst_color

def ImageProcess(files,pgcolor,pscolor,image_count):
    for file in files:
        picture: np.ndarray
        if(pgcolor == 1):
            picture = PencilSketch(cv.imread(file),True)
            cv.imwrite(f"Sketch_Image_{image_count}.jpg", picture)
            print(f"Sketch {image_count} Created")
            image_count += 1
            
        elif(pscolor == 1):
            picture = PencilSketch(cv.imread(file),False)
            cv.imwrite(f"Sketch_Image_{image_count}.jpg", picture)
            print(f"Sketch {image_count} Created")
            image_count += 1
        else:
            picture = cv.imread(file)
            gray_pic = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
            img_invert = cv.bitwise_not(gray_pic)
            gblur_img = cv.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
            dodged_img = cv.divide(gray_pic, 255 - gblur_img, scale=256)
            cv.imshow("last", dodged_img)

            cv.imwrite(f"Sketch_Image_{image_count}.jpg", dodged_img)
            print(f"Sketch {image_count} Created")
            
            image_count += 1
