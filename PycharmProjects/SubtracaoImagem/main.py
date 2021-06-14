import cv2

img_1 = cv2.imread('Aula 3 - Ex4.1.jpg', 0)
img_2 = cv2.imread('Aula 3 - Ex4.2.jpg', 0)

img_3 = img_1 - img_2

cv2.imshow("Imagem 1", img_1)
cv2.imshow("Imagem 2", img_2)
cv2.imshow("Subtração de img1 - img2", img_3)

cv2.waitKey(0)
cv2.destroyAllWindows()
