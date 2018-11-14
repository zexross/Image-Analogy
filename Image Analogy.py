import cv2
import numpy as np,sys
A = cv2.imread('E:\Digital Electronics\lf.tar\lf\lf-web\images\darkclouds.png')
B = cv2.imread('E:\Digital Electronics\lf.tar\lf\lf-web\images\oxbow.png')
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(0,4):
    G = cv2.pyrDown(G)
    gpA.append(G)
cv2.imwrite('E:\Digital Electronics\lf.tar\lf\lf-web\images\darkclouds3.png',gpA[3])
size = np.shape(gpA[4])
print(size)
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(0,4):
    G = cv2.pyrDown(G)
    gpB.append(G)
    
    
text = open('E:\Image Analogies\image data.txt' , 'w')
send = ''.join(str(e) for e in gpA[4])
text.write(send)
text.close()
