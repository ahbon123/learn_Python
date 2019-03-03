#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://blog.csdn.net/qq_29023939/article/details/81101168
# https://www.smwenku.com/a/5b8783812b71775d1cd790e2
# https://stackoverflow.com/questions/32970397/opencv-errorsizes-of-input-arguments-do-not-match/54966301#54966301

import cv2
import numpy as np,sys

A = cv2.imread('trump1.png')
B = cv2.imread('kim.png')

A = cv2.resize(A, (300, 400))
B = cv2.resize(B, (300, 400)) 

print(type(A))
# generate Gaussian pyramid for A
G = A.copy()
print(G)
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)
lpA = [gpA[5]]
for i in range(6,0,-1):
    print(i)
    GE = cv2.pyrUp(gpA[i])
    GE=cv2.resize(GE,gpA[i - 1].shape[-2::-1])
    L = cv2.subtract(gpA[i-1],GE)
    print(L.shape)
    lpA.append(L)
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(6,0,-1):
    print(i)
    GE = cv2.pyrUp(gpB[i])
    GE = cv2.resize(GE, gpB[i - 1].shape[-2::-1])
    L = cv2.subtract(gpB[i-1],GE)
    print(L.shape)
    lpB.append(L)
# Now add left and right halves of images in each level
LS = []
lpAc=[]
for i in range(len(lpA)):
    b=cv2.resize(lpA[i],lpB[i].shape[-2::-1])
    print(b.shape)
    lpAc.append(b)
print(len(lpAc))
print(len(lpB))
j=0
for i in zip(lpAc,lpB):
    print(i)
    la,lb=i
    print(la)
    print(lb)
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    j=j+1
    print(j)
    LS.append(ls)
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_= cv2.resize(ls_, LS[i].shape[-2::-1])
    ls_ = cv2.add(ls_, LS[i])
# image with direct connecting each half
B= cv2.resize(B, A.shape[-2::-1])
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))
cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
