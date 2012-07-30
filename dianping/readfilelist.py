#-*- coding:utf-8 -*-

f = file('area00.txt','r')
urlList = []
i=0
for line in f:
    a = line[:-1]
    if 'http'not in a:
        a = 'http://www.dianping.com' + a
    if a not in urlList:
        urlList.append(a)

f.close()
print urlList
print len(urlList)
file2 = file('area1.txt','w')
file2.write(str(urlList))
file2.close()
