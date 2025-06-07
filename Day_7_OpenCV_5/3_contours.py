import cv2
import os

# Step 1: Load the image
image_path = os.path.join(".", "images_", "vehicle.jpg")
vehicle_image = cv2.imread(image_path)

# Safety check: If image loading fails
if vehicle_image is None:
    print("Error: Image not found or path incorrect.")
    exit()

# Step 2: Convert to Grayscale
gray_image = cv2.cvtColor(vehicle_image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Binary Inverse Thresholding
# All pixels < 110 → white (255), else black (0)
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

# Step 4: Find contours (only external boundaries)
contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cvt in contours:
    if cv2.contourArea(cvt) > 200:
        # Step 5: Draw all contours on original image
        # cv2.drawContours(vehicle_image, cvt, -1, (0, 255, 0), thickness=2)
    # print(cv2.contourArea(cvt))

        x , y , w , h = cv2.boundingRect(cvt)
        cv2.rectangle(vehicle_image,(x,y),(x+w , y+w),(255,0,0),2)

# Step 6: Display the result
cv2.imshow("Contour Image", vehicle_image)
cv2.imshow("Threshold Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
