import cv2,sys

imagePath ="C:/Users/chait/projects/Python/face_recognition/aggarwal_group_2019.jpg"
cascPath = "C:/Users/chait/projects/Python/face_recognition/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=15,
)
print ("Found {0} faces!".format(len(faces)))


# Draw a rectangle around the faces
rectcolor = (255,255,0) #green
rectthickness = 2
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), rectcolor, rectthickness)

# resize image
#dim = (width, height)
scale_factor = 0.3
resized_image = cv2.resize(image, None, fx=scale_factor,fy=scale_factor)



cv2.imshow("Faces found", image)

cv2.waitKey(0)
cv2.destroyAllWindows()