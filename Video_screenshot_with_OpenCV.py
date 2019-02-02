import os
path = "E:/img/"
os.chdir(path)
os.getcwd()

filepath = 'E:/img' #视频所在文件夹
pathDir = os.listdir(filepath)

a = 1 #图片计数

for allDir in pathDir:
    videopath = 'E:/img/' + allDir
    print(videopath)
    
    vc =  cv2.VideoCapture(videopath) #读入视频文件
    c = 1
    
    if vc.isOpened(): #判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False
        
    timeF = 100 #视频帧计数间隔频率
    
    while rval: #循环读取视频帧
        rval, frame = vc.read()
        if (c%timeF == 0): #每隔timeF帧进行存储操作
            cv2.imwrite('./img/' + str(a) + '.jpg', frame)
            a = a + 1
        c = c + 1
        cv2.waitKey(1)
    vc.release()
