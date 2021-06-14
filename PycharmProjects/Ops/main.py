import cv2
img = cv2.imread("Abertura.bmp", 0)
img2 = cv2.imread("ee.bmp", 0)

abertura = cv2.morphologyEx(img, cv2.MORPH_OPEN, img2)

#intersecao = cv2.addWeighted(img, 0.4, erosao, 0.7, 1)
intersecao = cv2.bitwise_xor(img, abertura)

cv2.imshow("Img Original", img)
cv2.imshow("Img Abertura", abertura)
cv2.imshow("Intersecao", intersecao)

cv2.waitKey()
cv2.destroyAllWindows()

