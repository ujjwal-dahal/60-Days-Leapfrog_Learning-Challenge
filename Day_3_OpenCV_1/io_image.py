import os
import cv2

#read image

image_path = os.path.join(".","image","bird.png")

#os.path.join() le Each String lai Join garcha Seperated by \
#Example : mathiko -> .\image\bird.png Huncha


image = cv2.imread(image_path) #Esle Image lai read garcha ani Numpy Array ma Dincha


#write image

#imwrite(fileName , image)
#-> fileName means k dine file ko name i.e image ko name
#-> image means Numpy array wala formate ko image

cv2.imwrite(os.path.join(".","image","bird_out.png"),image)

#visualize image

cv2.imshow("image_frame",image)
#imshow() ko 1st Parameter is Window ko Name
#2nd Paremeter is Numpy Array wala Image
cv2.waitKey(0) #esle chai jaba samma user le kunai key press gardaina taba samma image dekhaune window lai open garcha
#yo waitKey() nadida openCV le some short second ko lagi open garcha image window jun user le dekhna paudaina
#esle parameter chai kati milisecond ko lagi Window Open garne
#0 value le chai indefinit time ko lagi open garcha user le key press nagarunjel






