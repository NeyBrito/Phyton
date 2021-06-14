# This is a sample Python script.
import cv2
import numpy as np

peppersColor = cv2.imread("peppers.png")
cv2.imshow("Imagem Colorida", peppersColor)

peppersNegativa = cv2.bitwise_not(peppersColor)
cv2.imshow("Imagem Negativa", peppersNegativa)

peppersCinza = cv2.cvtColor(peppersColor, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", peppersCinza)

cv2.waitKey(0)
cv2.destroyAllWindows()
