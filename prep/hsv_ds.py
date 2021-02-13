import cv2
import os

def cvrt_write(img_name,img_path,des_path):
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    des = os.path.join(des_path,img_name)
    cv2.imwrite(des, hsv)


failed_conversions = []
all_imgs = os.listdir('ds/RGB')

for img in all_imgs:
    img_path = os.path.join('ds/RGB/',img)
    try:
        cvrt_write(img,img_path,'ds/HSV/')
    except:
        failed_conversions.append(img)

print('FAILED CONVERSIONS : ',failed_conversions)
print(len(os.listdir('ds/HSV/')))



