import os

print("Current Working Directory:", os.getcwd())

import cv2
import os

# Print current working directory
print("Current Working Directory:", os.getcwd())

# Set full path to the background image
background_path = "C:/Users/nayan misal/voting system/online voting system by nayan/background.png"
print(f"Background image path: {background_path}")
imgBackground = cv2.imread(background_path)

# Check if the background image is loaded properly
if imgBackground is None:
    print(f"Background image not found at path: {background_path}")
    raise FileNotFoundError(f"Background image not found at path: {background_path}")
else:
    print("Background image loaded successfully")

# Example of using imgBackground in a larger script
video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    
    # Check if imgBackground is loaded and assign frame
    if imgBackground is not None:
        imgBackground[370:370 + 480, 225:225 + 640] = frame

    cv2.imshow('frame', imgBackground)
    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
        break

video.release()
cv2.destroyAllWindows()
