#https://www.jianshu.com/p/b4c87aa6fd24

#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import shutil

# 将文件内容拷贝到另一个文件中
shutil.copyfileobj(open('old.txt', 'r'), open('new.txt', 'w'))

# 拷贝文件
shutil.copyfile('old.txt', 'old1.txt')

# 仅拷贝权限。内容、组、用户均不变
shutil.copymode('old.txt', 'old1.txt')

# 复制权限、最后访问时间、最后修改时间
shutil.copystat('old.txt', 'old1.txt')

# 复制一个文件到一个文件或一个目录
shutil.copy('old.txt', 'old2.txt')

# 在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了
shutil.copy2('old.txt', 'old2.txt')

# 把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.copytree('C:/Users/xiaoxinsoso/Desktop/aaa', 'C:/Users/xiaoxinsoso/Desktop/bbb')

# 移动目录或文件
shutil.move('C:/Users/xiaoxinsoso/Desktop/aaa', 'C:/Users/xiaoxinsoso/Desktop/bbb') # 把aaa目录移动到bbb目录下

# 删除一个目录
shutil.rmtree('C:/Users/xiaoxinsoso/Desktop/bbb') # 删除bbb目录
