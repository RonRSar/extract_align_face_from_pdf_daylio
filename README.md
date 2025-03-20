# Face Extractor and Aligner from PDF 

This project was born out of frustration that I had to manually align my face when I was exporting files from Daylio to do my 1 Picture A Day compilations.

I used the FaceAligner class from [PyImageSearch](https://pyimagesearch.com/). The facial recognition model is from [dlib](https://dlib.net/face_landmark_detection.py.html).

## Prequisites
Install relevant python libraries.
```
pip install opencv-python dlib imutils fitz
```

## Instructions
1. Clone git repo
2. Insert a pdf file into working directory that contains images of faces
3. Change 'daylio_path' in ML_Face_Extractor.py
4. Run ML_Face_Extractor.py
