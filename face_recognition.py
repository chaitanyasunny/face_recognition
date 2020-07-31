import face_recognition

imagePath ="C:/Users/chait/projects/Python/face_recognition/aggarwal_group_2019.jpg"

image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)