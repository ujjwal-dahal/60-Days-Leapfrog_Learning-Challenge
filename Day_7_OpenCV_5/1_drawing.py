import os
import cv2


whiteboard = cv2.imread(os.path.join(".","images_","whiteboard.jpg"))

#line
starting_point = (230,450)
ending_point = (530,450)
color = (133,7,147) #in bgr formate
thickness = 3
cv2.line(whiteboard,starting_point,ending_point, color , thickness)


#rectangle
top_left_corner = (50,50)
bottom_right_corner = (250,250)
color = (183,29,12)
thickness =3
cv2.rectangle(whiteboard,top_left_corner,bottom_right_corner,color,thickness)

#circle
center = (450,250)
radius = 100
thickness = -1 #negative value le chai Fill garne kaam garcha 
#positive value le chai thickness lai increase garne kaam garcha
color = (2,63,22)
cv2.circle(whiteboard,center,radius,color,thickness)


#text
text = 'Hello World'
bottom_left_corner = (350,50)
font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 1
color = (73,14,201)
thickness =2
line_type =cv2.LINE_AA 
cv2.putText(whiteboard,text,bottom_left_corner,font,font_scale,color,thickness,line_type)

cv2.imshow("Whiteboard",whiteboard)
cv2.waitKey(0)
cv2.destroyAllWindows()
