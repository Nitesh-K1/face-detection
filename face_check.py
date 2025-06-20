import face_recognition
known_image = face_recognition.load_image_file("images/known.jpg")
test_image = face_recognition.load_image_file("images/test.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]
test_encoding = face_recognition.face_encodings(test_image)[0]
results = face_recognition.compare_faces([known_encoding], test_encoding)
distance = face_recognition.face_distance([known_encoding], test_encoding)[0]
print(f"Face Match: {results[0]}")
print(f"Confidence Score (lower is better): {distance:.4f}")
