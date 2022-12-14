import cv2
import numpy as np
import serial
import time
serialcomm = serial.Serial('COM4', 9600)
serialcomm.timeout = 1
c = 0
n = 0
m = 0


def callback(x):
    pass


# cap = cv2.VideoCapture(1)
cv2.namedWindow('image')
cv2.namedWindow('image1')

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change
# cv2.createTrackbar('lowH', 'image', ilowH, 179, callback)
# cv2.createTrackbar('highH', 'image', ihighH, 179, callback)

# cv2.createTrackbar('lowS', 'image', ilowS, 255, callback)
# cv2.createTrackbar('highS', 'image', ihighS, 255, callback)

# cv2.createTrackbar('lowV', 'image', ilowV, 255, callback)
# cv2.createTrackbar('highV', 'image', ihighV, 255, callback)


while True:
    # grab the frame
    # ret, frame = cap.read()

    frame = cv2.imread('C://Users//Aman Sagar//Downloads//dirty.jpg')
    frame1 = cv2.imread('C://Users//Aman Sagar//Downloads//clear.jpg')

    # get trackbar positions
    # ilowH = cv2.getTrackbarPos('lowH', 'image')
    # ihighH = cv2.getTrackbarPos('highH', 'image')
    # ilowS = cv2.getTrackbarPos('lowS', 'image')
    # ihighS = cv2.getTrackbarPos('highS', 'image')
    # ilowV = cv2.getTrackbarPos('lowV', 'image')
    # ihighV = cv2.getTrackbarPos('highV', 'image')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([23, 53, 84])
    higher_hsv = np.array([31, 135, 255])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    mask1 = cv2.inRange(hsv1, lower_hsv, higher_hsv)

    frame = cv2.bitwise_and(frame, frame, mask=mask)
    frame1 = cv2.bitwise_and(frame1, frame1, mask=mask1)
    # edges = cv2.Canny(mask, 50, 150, apertureSize=3)

    # show thresholded image

    cv2.imshow('image', frame)
    cv2.waitKey(10)
    cv2.imshow('image1', frame1)
    i, j = mask.shape
    per = c/(i*j)*100

    if n == 0:
        print(i, j)
        print(mask.shape)
        print(mask.any())
        for i in range(i):
            for j in range(j):
                if(mask[i][j] == 255):
                    c = c+1
        n = 1
        per = c/(i*j)*100
        print(per)
        print(c)
    i, j = mask1.shape

    if m == 0:
        print(i, j)
        print(mask.shape)
        print(mask.any())
        for i in range(i):
            for j in range(j):
                if(mask1[i][j] == 255):
                    c = c+1
        m = 1
        per = c/(i*j)*100
        print(per)
        print(c)

    # i = input("input(on/off): ").strip()
    if per > 10:
        i1 = 'off'
    if i1 == 'done':
        print('finished program')
        break
    serialcomm.write(i1.encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))

    serialcomm.close()

    k = cv2.waitKey(1000) & 0xFF  # large wait time to remove freezing
    if k == 113 or k == 27:
        break


cv2.destroyAllWindows()

# cap.release()
