import cv2
clicked = False
def onMouse(event,x,y,flags,param)
global clicked
if event == cv2.cv.CV_EVENT_LBUTTONUP:
    clicked = True
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)