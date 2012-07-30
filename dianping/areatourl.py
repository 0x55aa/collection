#-*- coding:utf-8 -*-
import cookielib, urllib2
from BeautifulSoup import BeautifulSoup
import re
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
 
            #print html
            soup = BeautifulSoup(html)

            list2 = soup.find('ul',attrs={'class':re.compile("current")})
            #list3 = list2.findAll('a',attrs={'href':re.compile(self.t_url[23:-4])})
            list3 = list2.findAll('a')

            namelist = []
            urllist = []
            for i in list3:
                namelist.append(i.contents[0][:-6])
                urllist.append( i["href"])
            #print len(namelist),len(urllist)
            #print namelist,urllist
            if len(namelist)==len(urllist):
                return namelist,urllist
            else:
                print "error~~~"


        except urllib2.URLError:
            print('connection error')


if __name__ == '__main__':#eval(myStr)
    
    f = file('area3.txt','r')
    snameList = eval(f.readline())
    surlList = eval(f.readline())
    
    f.close()
    #print snameList,surlList
    
    file2 = file('aaa24.txt','w+')
    for i in range(len(surlList)):
        file2.write(snameList[i].encode("utf-8"))
        file2.write('\n')
        for i in range(len(surlList)):
            t = T_list("http://www.dianping.com"+surlList[i])
            namelist,urllist = t.get_subject_list()
            
            file2.write(str(namelist))
            file2.write('\n')
            file2.write(str(urllist))
            file2.write('\n')
            print i

    file2.close()
    
    """
    url = "http://www.dianping.com/search/category/79/45/r353"
    t = T_list(url)
    t.get_subject_list()
    """
    
