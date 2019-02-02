#https://blog.csdn.net/qq_34510308/article/details/85297800

#读取中文路径
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8),-1)
    return cv_img
file_path = 'C:/测试/Test.jpg'
img = cv_imread(file_path)
print(img)

#保存中文路径
def cv_imwrite(savePath,tem):
    cv2.imencode('.jpg',tem)[1].tofile(savePath)  # 保存图片

#https://blog.csdn.net/liuqinshouss/article/details/78696032

# -*- coding: utf-8 -*-
import cv2
import numpy as np
 
## 读取图像，解决imread不能读取中文路径的问题
def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img
if __name__=='__main__':
    path='E:/images/百合/百合1.jpg'
    img=cv_imread(path)
    cv2.namedWindow('lena',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('lena',img)
    k=cv2.waitKey(0)
    ##这样是保存到了和当前运行目录下
    cv2.imencode('.jpg', img)[1].tofile('百合.jpg')
