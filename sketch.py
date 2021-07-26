import os
import cv2 as cv
import sys
import numpy as np
import argparse
from image import Processing


def main():
    video_id: int = 0
    red_args:int = 0
    green_args:int = 0
    blue_args:int = 0
    pgcolor:int = 0
    pscolor:int = 0
    picture_enabled:bool = False

    arg_parser = argparse.ArgumentParser(description="Sketch App")
    arg_parser.add_argument("-v", "--videocapture", metavar="<Video ID>", type=int, help="Select Camera")
    arg_parser.add_argument("-p", "--picture", metavar="-p picture", type=str, help="Choose picture")

    arg_parser.add_argument("-pgc", "--pgcolor", metavar="<-pgc 0|1 >", type=int, help="Enable Colorful Pencil Sketch")
    arg_parser.add_argument("-psc", "--pscolor", metavar="<-psc 0|1 >", type=int, help="Enable Grayscale Pencil Sketch")

    # TODO: This params could be change
    arg_parser.add_argument("-r", "--red", metavar="<red color code>", type=int, help="Red Color Code")
    arg_parser.add_argument("-b", "--blue", metavar="<blue color code>", type=int, help="Blue Color Code")
    arg_parser.add_argument("-g", "--green", metavar="<green color code>", type=int, help="Green Color Code")

    args = arg_parser.parse_args()

    pgcolor = args.pgcolor
    pscolor = args.pscolor

    if bool(args.red):
        print(args.red)
        red_args = args.red
    
    if bool(args.green):
        print(args.green)
        red_args = args.green

    if bool(args.blue):
        print(args.blue)
        red_args = args.blue
    


    if(pgcolor == 1 and pscolor == 1):
        print("Grayscale and Colorful Pencil Sketch can't use at the same time")
        sys.exit()

    videocapture_arg:int = args.videocapture
    picture:str = args.picture
    if picture == None or picture == "":
        if videocapture_arg >= 0:
            print(f"Video mode: {videocapture_arg}")
            video_id = videocapture_arg
            VideoMode(video_id,pgcolor,pscolor)
    else:
        picture_enabled = True
        print(f"Picture mode: {picture}")
        PictureMode(picture,pgcolor,pscolor)

def PictureMode(png:str,pgcolor:int,pscolor:int):
    files:list[str]  = []
    files.append(png)
    image_count:int = 0
    Processing.ImageProcess(files,pgcolor,pscolor,image_count)


def VideoMode(video_id,pgcolor,pscolor) -> None:
    videocapture = cv.VideoCapture(video_id)
    if videocapture.isOpened() is False:
        print("The Camera ID you choose cannot open. It could be used by other programs or unavailable camera,exiting.")
        sys.exit()

    cv.namedWindow("Sketch Generator")
    image_count: int = 0
    print("To capture an image, press SpaceBar otherwise press Esc Key to Exit")

    while True:
        check: bool
        frame: np.ndarray
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
    path: str = "./"

    # TODO : Fix Duplicate result bug problem.
    files: list = []
    for root, _ ,file in os.walk(path):
        for f in file:
            if ".jpg" in f:
                files.append(os.path.join(root, f))

    Processing.ImageProcess(files,pgcolor,pscolor,image_count)

    print("Thank you for using Sketch Converter!")




if __name__ == "__main__":
    main()
