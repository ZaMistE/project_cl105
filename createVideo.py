from turtle import shape
import cv2
import os

path = "Images"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jfif']:
        file_name = path+"/"+file
        images.append(file_name)

count = len(images)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(0, count):
    print(images[i])
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done")