#-*- coding:utf-8 -*-
import cookielib, urllib2
from BeautifulSoup import BeautifulSoup

class T_list:
    
    def __init__(self,url):
        self.t_url = url
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
        self.urlList = []
        self.areaList = []
    def get_subject_list(self):
        try:
            #html = urllib2.urlopen(self.t_url).read()
            
            f = file('b.htm','r')
            html = f.read()
            f.close()
        
            soup = BeautifulSoup(html)
            #print soup.title
            
            list1 = soup.findAll('a')
            for i in list1:
                #print i.string
                self.areaList.append(i.string)
                #print str(i["href"])
                self.urlList.append(i["href"])

            file2 = file('area0.txt','w+')
            file2.write(str(self.areaList))
            file2.write('\n')
            file2.write(str(self.urlList))
            file2.close()

            print len(self.areaList),len(self.urlList)

        except urllib2.URLError:
            print('connection error')


if __name__ == '__main__':#eval(myStr)
    url = "http://www.dianping.com/citylist"
    t = T_list(url)
    
    t.get_subject_list()

