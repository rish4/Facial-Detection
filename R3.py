import cv2 as cv

# Read image from your local file system
img_path='C:/Users/Rishita/Downloads/download (1).jpg'
original_image = cv.imread(img_path)


# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)


path_haar='C:/Users/Rishita/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml'
face_cascade = cv.CascadeClassifier(path_haar)


detected_faces = face_cascade.detectMultiScale(grayscale_image)

for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )
    
cv.imshow('Image', original_image)
cv.waitKey(0)

    