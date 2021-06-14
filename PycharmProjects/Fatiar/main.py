import cv2

img1 = cv2.imread('Conjunto_A.jpg')
img2 = cv2.imread('Conjunto_B.jpg')

cv2.imshow('Img 1 Original', img1)
cv2.imshow('Img 2 Original', img2)

uniao = cv2.bitwise_and(img1, img2, mask = None)
cv2.imshow('Uniao', uniao)

intersecao = cv2.bitwise_xor(img1, img2, mask = None)
cv2.imshow('Intesecao', intersecao)

cv2.waitKey(0)
cv2.destroyAllWindows()