import os
import cv2

picture = cv2.VideoCapture(0)
cv2.namedWindow("Sketch Generator")
image_count = 0
print("To capture an image, press SpaceBar otherwise press Esc Key to Exit")

while True:
    check, frame = picture.read()
    if check is False:
        print("The Camera failed to get detected. \n Please check your settings.")
    cv2.imshow("Sketch Generator", frame)
    key = cv2.waitKey(1)
    ## Space Bar Key is used to Capture the image
    ## Esc Key is used to exit the frame
    if key%256 == 32: #Space key
        name = "Original_Image_{}.jpg".format(image_count)
        cv2.imwrite(name, frame)
        print("Image {} Captured".format(image_count))
        image_count +=1
    elif key%256 == 27: #Esc Key
        print("You have pressed an escape key, Exiting!")
        break

picture.release()
cv2.destroyAllWindows()

#reading all the original captured files from the current directory
path = './'

files = []
for root, directory, file in os.walk(path):
    for f in file:
        if ".jpg" in f:
            files.append(os.path.join(root,f))
background = cv2.imread("White.png", cv2.CV_8UC1)
background = cv2.resize(background, (500, 500))
image_count = 0

for f in files:
    picture = cv2.imread(f)
    picture = cv2.resize(picture, (500, 500))
    scale = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    invert = 255 - scale
    smoothen = cv2.GaussianBlur(invert, ksize=(21, 21), sigmaX=0, sigmaY=0)
    blend_with_background = cv2.divide(scale, 255 - smoothen, scale=256)
    sketch = cv2.multiply(blend_with_background, background, scale=1 / 256)
    cv2.imwrite('Sketch_Image_{}.jpg'.format(image_count), sketch)
    print('Sketch {} Created'.format(image_count))
    image_count +=1

print("Thank you for using Sketch Converter!")
