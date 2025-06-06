
import os
import cv2


image_path = os.path.join(".","images","person_image.jpg")



person_image = cv2.imread(image_path)
image = person_image
# print(image.shape)

# #resizing
scaled_percent = 30 
width = image.shape[1] * scaled_percent / 100
width = int(width)
height = image.shape[0] * scaled_percent / 100
height = int(height)
# print(type(width),width)
# print(type(height),height)


resized_person_image = cv2.resize(person_image,(width,height))


#classical Blur -> Most Commonly used
k_size = 11 #Esle Determine garcha ki Blur ko strength
#i.e Internally esle chai kati far samma ko Neighbour Pixel ko Value lai average garne ho bhanne bhancha

classical_blur = cv2.blur(resized_person_image,(k_size,k_size))
# cv2.imshow("Classical Blured Image",classical_blur)

gaussian_blur = cv2.GaussianBlur(resized_person_image, (k_size,k_size),0)
#gaussian blur lai k size odd hunu parcha
# cv2.imshow("Gaussian Blur",gaussian_blur)



#median blur le salt & pepper noise remove garcha
salt_pepper_noise_image = cv2.imread(os.path.join(".","images","salt_and_pepper_noise_image.jpeg"))
salt_pepper_noise_image = cv2.resize(salt_pepper_noise_image,None , fx=1,fy=1) #fx & fy are scale factor
cv2.imshow("Salt & Pepper Noise Image",salt_pepper_noise_image)

k_size_median = 5
noise_removed = cv2.medianBlur(salt_pepper_noise_image,k_size_median)
cv2.imshow("Noise Removed Image",noise_removed)

median_blur = cv2.medianBlur(resized_person_image,k_size)
# cv2.imshow("Median Blur",median_blur)

# cv2.imshow("Without Bluring",resized_person_image)
cv2.waitKey(0)

