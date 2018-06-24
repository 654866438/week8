
#难度不大，idea就是在loop里再循环一个loop去搜索

import sys

# 如果元素数量 《 2 的情况

if len(sys.argv) < 3:

    print('Cannot process')

    sys.exit(0)

#找到文件名

file = sys.argv[1]

#读取单词名

word = sys.argv[2]

#打开文件，载入阅读模式

fptr = open(file , 'r')

count = 0

#给x设置为所读取文件的内容

x = fptr.read()

#然后对每行进行读取，这是第一个loop

for line in x.split('\n'):

#每一行里又分别对每一个词进行读取，这是第二个loop

    for w in line.split(' '):

        # 这里可以扩展一下

        # 如果要搜索的和给定的一样，数量+1

        if w == word:

       

            count += 1

           

if count == 0:

    print('\"'+word.rstrip("/n")+'\" does not exist in this file')

   

else:

    print('\"'+word.rstrip("/n")+'\"','has been found',count,'times')

