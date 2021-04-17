import cv2
import os

def multiScale(img_name,img_path,des_path):
    img = cv2.imread(img_path)
    dim = img.shape[0]
    downscale1 = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    downscale2 = cv2.resize(downscale1, (0, 0), fx=0.5, fy=0.5)
    des_directory = os.path.join(des_path,img_name)
    os.mkdir(des_directory)
    des1 = des_directory+"//256_256.jpg"
    des2 = des_directory + "//128_128.jpg"
    des3 = des_directory + "//64_64.jpg"
    cv2.imwrite(des1, img)
    cv2.imwrite(des2, downscale1)
    cv2.imwrite(des3, downscale2)



failed_conversions = []
all_imgs = os.listdir('D:\work\CompressX\ds\RGB')

for img in all_imgs:
    img_path = os.path.join('D:\work\CompressX\ds\RGB',img)
    des_path = 'D:\work\CompressX\ds\multiscale'
    try:
        img_name = img.replace('.jpg','')
        multiScale(img_name,img_path,des_path)
    except:
        failed_conversions.append(img)

print('FAILED CONVERSIONS : ',failed_conversions)

