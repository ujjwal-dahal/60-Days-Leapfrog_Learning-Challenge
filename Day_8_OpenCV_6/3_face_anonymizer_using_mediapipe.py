import cv2
import mediapipe as mp

# Start webcam
webcam = cv2.VideoCapture(0)

# Initialize MediaPipe face detection once
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

while True:
    _, person_image = webcam.read()
    if not _: break

    # Convert BGR to RGB for MediaPipe
    image_rgb = cv2.cvtColor(person_image, cv2.COLOR_BGR2RGB)
    result = face_detection.process(image_rgb)

    if result.detections:
        h, w, _ = person_image.shape
        for detection in result.detections:
            bbox = detection.location_data.relative_bounding_box

            # Convert to absolute pixel coordinates
            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            box_width = int(bbox.width * w)
            box_height = int(bbox.height * h)

            # Blur detected face
            crop_face = person_image[y:y + box_height, x:x + box_width]
            blur_face = cv2.GaussianBlur(crop_face, (51, 51), 0)
            person_image[y:y + box_height, x:x + box_width] = blur_face

            # Optional: Draw rectangle
            cv2.rectangle(person_image, (x, y), (x + box_width, y + box_height), (255, 0, 0), 1)

    # Show result
    cv2.imshow("Webcam Face Blur", person_image)

    # Exit on 'q' key
    if cv2.waitKey(4) & 0xFF == ord("q"):
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()
