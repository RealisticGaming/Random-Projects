import cv2

img = cv2.imread('babypandas.jpg')
BW = cv2.imread('babypandas.jpg')
co = cv2.imread('babypandas.jpg')

cv2.imshow('babypandas', img)

key = cv2.waitKey(5000)
cv2.destroyAllWindows()

paint = str(input("What way would you like it?\n1.Original\n2.B&W\n3.Colors\nOr just type 'exit' to leave\n"))

while paint != "exit":
   if paint == "1":
       cv2.imshow('babypandas', img)
   elif paint == "2":
       BW = cv2.cvtColor(BW, cv2.COLOR_BGR2GRAY)
       cv2.imshow('babypandas', BW)
   elif paint == "3":
       co = cv2.cvtColor(co, cv2.COLOR_BGR2YUV)
       cv2.imshow('babypandas', co)
   cv2.waitKey(5000)
   cv2.destroyAllWindows()
   paint = str(input("What way would you like it?\n1.Original\n2.B&W\n3.Colors\nOr just type 'exit' to leave\n"))

print("I hope you liked the presentation of colors")

