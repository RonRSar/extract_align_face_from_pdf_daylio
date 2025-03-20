import os

import dlib
import cv2

from extract_img_from_pdf import extract_img_from_pdf

# from pythonimagesearch tutorial 
from imutils import face_utils, resize


# Change these to control parameters
daylio_file = "\daylio_export_2025_03_19.pdf" #ensure in working dir
path = os.getcwd()
# image resolution
desiredFaceHeight = 651
desiredFaceWidth = 365

# get files in dir (default path = cwd)
if not any("daylio_image" in file for file in os.listdir(path)):
      #ensure daylio export photos
      extract_img_from_pdf(daylio_file)
images = []
for file in os.listdir(path):
        if file.endswith(".jpeg") and "image" in file:
                images.append(os.path.join(path, file))

# Sort files by numerical index as str '10' > '2'
def get_file_index(file):
    return int(file.split('image_')[1].strip('.jpeg'))

images = sorted(images, key=get_file_index) 

# use the face shape predictor and detector from dlib 
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)
fa = face_utils.FaceAligner(predictor, desiredFaceHeight=desiredFaceHeight, desiredFaceWidth=desiredFaceWidth)

failed_face = []

for i, image_path in enumerate(images):
    print(f"Read: {image_path.split('Collage\\')[1]}")

    image = cv2.imread(image_path)

    # load the input image and convert it to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    # detect faces in the grayscale image
    rects = detector(gray, 0)

    # some faces wont be detected
    if len(rects) == 0:
          failed_face.append(image_path.split('Collage\\')[1])
          faceAligned = resize(image, width=365, height=651)
    else:
        for rect in rects:
            #edit the imutils align func to change more 
            faceAligned = fa.align(image, gray, rect, borderValue=(64,64,64))

    image_name = "aligned_" + str(i) + ".jpeg"
    cv2.imwrite(image_name, faceAligned)

    print(f"Saved: {image_name}")

#see which ones failed
print(f"Total Failed: {len(failed_face)}")
for failed_file in failed_face:
    print(f"Failed: {failed_file}")



