import os
from typing import Literal
import cv2 as cv
import sys
import getopt
import numpy

def help():
    print("Usage : sketch.py -v <Camera ID>")
    sys.exit()

def main(argv):
    video_id: int = -1
    try:
        opts, args = getopt.getopt(sys.argv[1:], "v", ["videocapture="])
        if len(argv) != 0:
            if argv[0] != "-v":
                help()
            elif argv[0] != "--videocapture":
                help()
        else:
            help()

    except getopt.GetoptError:
        help()
    for opt, arg in opts:
        if opt == "-h":
            help()
        elif opt in ("-v", "--videocapture"):
            if arg.isdigit():
                video_id = int(arg)
            else:
                print("Camera ID Value must be positive and integer")
                sys.exit()
        else:
            help()

    videocapture = cv.VideoCapture(video_id)
    if videocapture.isOpened() is False:
        print("The Camera ID you choose cannot open the camera,exiting.")
        sys.exit()

    cv.namedWindow("Sketch Generator")
    image_count: int = 0
    print("To capture an image, press SpaceBar otherwise press Esc Key to Exit")

    while True:
        check: bool
        frame: numpy.ndarray
        check, frame = videocapture.read()
        if check is False:
            print("The Camera failed to get detected. \n Please check your settings.")
            sys.exit()

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
    path: Literal = "./"

    files: list = []
    for root, file in os.walk(path):
        print(file)
        print(root)
        for f in file:
            if ".jpg" in f:
                files.append(os.path.join(root, f))
    image_count: int = 0

    file: str
    for file in files:
        picture: numpy.ndarray = cv.imread(file)
        gray_pic = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
        img_invert = cv.bitwise_not(gray_pic)
        gblur_img = cv.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
        dodged_img = cv.divide(gray_pic, 255 - gblur_img, scale=256)
        cv.imshow("last", dodged_img)
        cv.imwrite(f"Sketch_Image_{image_count}.jpg", dodged_img)
        print(f"Sketch {image_count} Created")
        image_count += 1

    print("Thank you for using Sketch Converter!")


if __name__ == "__main__":
    main(sys.argv[1:])
