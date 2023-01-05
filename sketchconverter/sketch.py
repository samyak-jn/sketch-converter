import os
from sys import exit as sys_exit

import cv2 as cv
import numpy as np


def PencilSketch(img: np.ndarray, isGray: bool = False) -> np.ndarray:
    dst_gray: np.ndarray
    dst_color: np.ndarray
    # TODO: Gray and Color param need adjusment
    dst_gray, dst_color = cv.pencilSketch(
        img, sigma_s=60, sigma_r=0.07, shade_factor=0.05
    )
    if isGray is True:
        return dst_gray
    else:
        return dst_color


def ImageProcess(files, pgcolor, pscolor, image_count: int = 0):
    for file in files:
        picture: np.ndarray
        if pgcolor == 1:
            picture = PencilSketch(cv.imread(file), True)
            cv.imwrite(f"Sketch_Image_{image_count}.jpg", picture)
            print(f"Sketch {image_count} Created")
            image_count += 1

        elif pscolor == 1:
            picture = PencilSketch(cv.imread(file), False)
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


def CameraProcess(pgcolor, pscolor, video_src: int = 0):
    videocapture = cv.VideoCapture(video_src)
    if videocapture.isOpened() is False:
        print(
            """The Camera ID you choose cannot open. \
            It could be used by other programs or \
            unavailable camera,exiting."""
        )
        sys_exit()

    cv.namedWindow("Sketch Generator")
    image_count: int = 0
    print("To capture an image, press SpaceBar otherwise press Esc Key to Exit")

    while True:
        check: bool
        frame: np.ndarray
        check, frame = videocapture.read()
        if check is False:
            print("The Camera failed to get detected. \n Please check your settings.")
            sys_exit()

        cv.imshow("Sketch Generator", frame)
        key: int = cv.waitKey(1)
        ## Space Bar Key is used to Capture the image
        ## Esc Key is used to exit the frame
        if key % 256 == 32:  # Space key
            name: str = f"Original_Image_{image_count}.jpg"
            cv.imwrite(name, frame)
            print(f"Image {image_count} Captured")
            image_count += 1
        elif key % 256 == 27:  # Esc Key
            print("You have pressed an escape key, Exiting!")
            break

    videocapture.release()
    cv.destroyAllWindows()

    # reading all the original captured files from the current directory
    path: str = "./"

    # TODO : Fix Duplicate result bug problem.
    files: list = []
    for root, _, file in os.walk(path):
        for f in file:
            if ".jpg" in f:
                files.append(os.path.join(root, f))

    ImageProcess(files, pgcolor, pscolor, image_count)
