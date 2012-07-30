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

            list2 = soup.find('div',id = 'searchList')
            #店名获取
            list0 = list2.findAll('li',attrs={'class':re.compile("shopname")})
            namelist = []
            for i in list0:
                namelist.append(i.a.contents[0])

            #地址 电话 获取
            list1 = list2.findAll('li',attrs={'class':re.compile("address")})
            addrlist = []
            phonelist = []
            for i in list1:
                if i.a:
                    sr = i.a.contents[0] + i.contents[2]
                else:
                    sr = i.contents[1]
                #print sr
                srlist = sr.split('&nbsp;&nbsp;')
                if len(srlist) == 1:
                    addrlist.append('')
                    phonelist.append(srlist[0])
                else:
                    addrlist.append(srlist[0])
                    phonelist.append(srlist[1])
                
            #print addrlist, phonelist
            #print len(namelist),len(addrlist),len(phonelist)

            #下一页url
            list3 = list2.find('a',attrs={'class':re.compile("NextPage")})
            if list3:
                nexturl = list3['href']
            else:
                nexturl = ''
            #print nexturl

            if len(namelist)==len(addrlist) and len(phonelist)==len(addrlist):
                return namelist,addrlist,phonelist,nexturl
            else:
                print "error~~~"


        except urllib2.URLError:
            print('connection error')


if __name__ == '__main__':#eval(myStr)
    
    #读取文件
    f1 = file('area3.txt','r')
    #地区名单
    areaname = eval(f1.readline())
    f1.close()
    #地区个数
    thenum = len(areaname)
    print thenum
    f = file('aaa23.txt','r')
    line = f.readline()
    
    #输出
    file2 = file('00/aaa23.txt','w+')
                
    file2.write(str(thenum))
    file2.write('\n')
    for i in range(thenum):
    #for i in range(8,9):
            sportname = eval(f.readline())
            urllist = eval(f.readline())
            print areaname[i]
            print sportname,urllist
            #项目个数
            num = len(sportname)



            file2.write(areaname[i].encode('utf-8') +' '+str(num))
            file2.write('\n')
            for i in range(num):
                file2.write(sportname[i].encode('utf-8'))
                file2.write('\n')

                url = "http://www.dianping.com" + urllist[i]
                t = T_list(url)
                namelist,addrlist,phonelist,nexturl = t.get_subject_list()

                
                i=1
                print i
                while nexturl:
                    
                    tt = T_list("http://www.dianping.com"+nexturl)
                    namelist1,addrlist1,phonelist1,nexturl = tt.get_subject_list()
                    namelist+=namelist1
                    addrlist+=addrlist1
                    phonelist+=phonelist1
                    i+=1
                    print i

                file2.write(str(namelist))
                file2.write('\n')
                file2.write(str(addrlist))
                file2.write('\n')
                file2.write(str(phonelist))
                file2.write('\n')
                
    file2.close()
    f.close()
