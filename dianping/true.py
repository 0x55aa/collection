#-*- coding:utf-8 -*-
import cookielib, urllib2
from BeautifulSoup import BeautifulSoup

class T_list:
    
    def __init__(self,url):
        self.t_url = url
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5", 
             "Accept": "text/html"}
        self.req = urllib2.Request(self.t_url, headers=i_headers) 
    def get_subject_list(self):
        try:
            html = urllib2.urlopen(self.req).read()
            """
            f = file('b.htm','r')
            html = f.read()
            f.close()
            """
            #print html
            soup = BeautifulSoup(html)
            #print soup.title
            
            #list1 = soup.find('a', id="J_qs-channel")
            #print list1['data-value']
            list2 = soup.find('div', {'class':"J_mkt"})
            
            url = 'http://www.dianping.com/search/category/'+list2['data-mkt-cityid']+'/45/g0r0'
            return url
            """
            for i in list1:
                print i.string
                #print str(i["href"])

            
            asd = soup.find('div', id="productDescription")
            strasd = str(asd)
            aaa = BeautifulSoup(strasd)
            bbb = aaa.findAll('div', {'class':["leftImage","rightImage"]})
            for l in bbb:
                #
                #print str(l)
                strasd = strasd.replace(str(l),'')

            print strasd
            #商品特性
            print soup.find('td', {'class':"bucket normal"})

            #重要信息
            print soup.find('div', id="importantInformation")
            """

        except urllib2.URLError:
            print('connection error')


if __name__ == '__main__':#eval(myStr)
    f = file('area1.txt','r')
    surlList = eval(f.readline())
    f.close()
    print len(surlList)
    urlList = []
    for i in range(len(surlList)):
        t = T_list(surlList[i])
        urlList.append( t.get_subject_list())

    file2 = file('area2.txt','w')
    file2.write(str(urlList))
    file2.close()
    print urlList
    print len(urlList)
    

    """
    url = "http://www.dianping.com/haerbin/sports"
    t = T_list(url)
    t.get_subject_list()
    """
