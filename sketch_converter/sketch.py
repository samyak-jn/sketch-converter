from sys import exit as sys_exit

import numpy as np
from cv2 import (
    COLOR_BGR2GRAY,
    GaussianBlur,
    VideoCapture,
    cvtColor,
    destroyAllWindows,
    divide,
    imread,
    imshow,
    imwrite,
    namedWindow,
    pencilSketch,
    waitKey,
)


def ImageColorPencilSketch(files: list[str], image_count: int = 0) -> None:
    for file in files:
        picture: np.ndarray = imread(file)
        _, color = pencilSketch(
            picture, sigma_s=60, sigma_r=0.07, shade_factor=0.05
        )
        imwrite(f"Sketch_Image_{image_count}.jpg", color)
        print(f"Sketch {image_count} Created")


def ImageGrayScalePencilSketch(files: list[str], image_count: int = 0) -> None:
    for file in files:
        picture: np.ndarray = imread(file)
        gray_pic = cvtColor(picture, COLOR_BGR2GRAY)
        gblur_img = GaussianBlur(gray_pic, (21, 21), sigmaX=0, sigmaY=0)
        dodged_img = divide(gray_pic, 255 - gblur_img, scale=256)
        imwrite(f"Sketch_Image_{image_count}.jpg", dodged_img)
        print(f"Sketch {image_count} Created")


def _CameraCapture(video_src: int = 0, color_mode: bool = False) -> None:
    videocapture = VideoCapture(video_src)
    if videocapture.isOpened() is False:
        print(
            """The Camera ID you choose cannot open.\
            It could be used by other programs or\
            unavailable camera,exiting."""
        )
        sys_exit()

    namedWindow("Sketch Generator")
    print("Press SpaceBar to capture an image, or press Esc Key to Exit")
    count = 0

    while True:
        check: bool
        frame: np.ndarray
        check, frame = videocapture.read()
        if check is False:
            print("Cannot read the frame, exiting!")
            sys_exit()

        imshow("Sketch Generator", frame)
        key: int = waitKey(1)
        ## Space Bar Key is used to Capture the image
        ## Esc Key is used to exit the frame
        if key % 256 == 32:  # Space key
            name: str = "Original_ImageCapture.jpg"
            imwrite(name, frame)
            if color_mode:
                ImageColorPencilSketch([name], count)
                count += 1
            else:
                ImageGrayScalePencilSketch([name], count)
                count += 1
        elif key % 256 == 27:  # Esc Key
            print("You have pressed an escape key, Exiting!")
            break

    videocapture.release()
    destroyAllWindows()


def CameraGrayPencilSketch(video_src: int = 0) -> None:
    _CameraCapture(video_src, False)


def CameraColorPencilSketch(video_src: int = 0) -> None:
    _CameraCapture(video_src, True)
