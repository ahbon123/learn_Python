import subprocess
import os

src = r'D:\files'
dst = r'D:\files\mp4'

for root, dirs, filenames in os.walk(src, topdown=False):
    #print(filenames)
    for filename in filenames:
        if ".flv" in filename:
            inputfile = os.path.join(root, filename)
            #print(inputfile)
            outputfile = os.path.join(dst, filename.replace(".flv", ".mp4"))
            subprocess.run(['ffmpeg', '-i', inputfile, outputfile])  
