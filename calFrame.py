import cv2
import math


# if __name__ == '__main__':

#     video = cv2.VideoCapture("data/video/test5.mp4")

#     # Find OpenCV version
#     (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
#     print(f"{major_ver}, {minor_ver}, {subminor_ver}")

    

#     # print(math.degrees(math.atan(1.5)))
#     # print(math.degrees(1.4))

#     if int(major_ver) < 3:
#         fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
#         print(
#             "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
#     else:
#         fps = video.get(cv2.CAP_PROP_FPS)
#         print(
#             "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

#     video.release()


img = cv2.imread('test2.png')
print(img.shape)
cv2.circle(img,  (400,50), 1, (250, 0, 0), 5)
cv2.imwrite('image.jpg', img)
