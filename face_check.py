import face_recognition
known_image=face_recognition.load_image_file("images/known.jpg")
known_encoding=face_recognition.face_encodings(known_image)[0]

test_image=face_recognition.load_image_file("images/test.jpg")
test_encoding=face_recognition.face_encodings(test_image)[0]
results=face_recognition.compare_faces([known_encoding], test_encoding)
if results[0]:
    print("its a match same person.")
else:
    print("not a match. different person")