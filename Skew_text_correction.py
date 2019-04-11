# https://blog.csdn.net/u010379996/article/details/83088946
# -*- coding: UTF-8 -*-
 
import numpy as np
import cv2
 
## 图片旋转
def rotate_bound(image, angle):
    #获取宽高
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # 提取旋转矩阵 sin cos 
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # 计算图像的新边界尺寸
    nW = int((h * sin) + (w * cos))
#     nH = int((h * cos) + (w * sin))
    nH = h
 
    # 调整旋转矩阵
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    return cv2.warpAffine(image, M, (nW, nH),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
 
## 获取图片旋转角度
def get_minAreaRect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    return cv2.minAreaRect(coords)
 
image_path = "54321.png"
image = cv2.imread(image_path)
angle = get_minAreaRect(image)[-1]
rotated = rotate_bound(image, angle)
 
cv2.putText(rotated, "angle: {:.2f} ".format(angle),
    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
# show the output image
print("[INFO] angle: {:.3f}".format(angle))
cv2.imshow("imput", image)
cv2.imshow("output", rotated)
cv2.waitKey(0)

# https://blog.csdn.net/u013063099/article/details/81937848?utm_source=copy
# coding=utf-8
import cv2
import numpy as np
 
input_img_file = "../test/test.png"
 
# 度数转换
def DegreeTrans(theta):
    res = theta / np.pi * 180
    return res
 
# 逆时针旋转图像degree角度（原尺寸）
def rotateImage(src, degree):
    # 旋转中心为图像中心
    h, w = src.shape[:2]
    # 计算二维旋转的仿射变换矩阵
    RotateMatrix = cv2.getRotationMatrix2D((w/2.0, h/2.0), degree, 1)
    print(RotateMatrix)
    # 仿射变换，背景色填充为白色
    rotate = cv2.warpAffine(src, RotateMatrix, (w, h), borderValue=(255, 255, 255))
    return rotate
 
# 通过霍夫变换计算角度
def CalcDegree(srcImage):
    midImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    dstImage = cv2.Canny(midImage, 50, 200, 3)
    lineimage = srcImage.copy()
 
    # 通过霍夫变换检测直线
    # 第4个参数就是阈值，阈值越大，检测精度越高
    lines = cv2.HoughLines(dstImage, 1, np.pi/180, 200)
    # 由于图像不同，阈值不好设定，因为阈值设定过高导致无法检测直线，阈值过低直线太多，速度很慢
    sum = 0
    # 依次画出每条线段
    for i in range(len(lines)):
        for rho, theta in lines[i]:
            # print("theta:", theta, " rho:", rho)
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(round(x0 + 1000 * (-b)))
            y1 = int(round(y0 + 1000 * a))
            x2 = int(round(x0 - 1000 * (-b)))
            y2 = int(round(y0 - 1000 * a))
            # 只选角度最小的作为旋转角度
            sum += theta
            cv2.line(lineimage, (x1, y1), (x2, y2), (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imshow("Imagelines", lineimage)
 
    # 对所有角度求平均，这样做旋转效果会更好
    average = sum / len(lines)
    angle = DegreeTrans(average) - 90
    return angle
 
if __name__ == '__main__':
    image = cv2.imread(input_img_file)
    cv2.imshow("Image", image)
    # 倾斜角度矫正
    degree = CalcDegree(image)
    print("调整角度：", degree)
    rotate = rotateImage(image, degree)
    cv2.imshow("rotate", rotate)
    # cv2.imwrite("../test/recified.png", rotate, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
