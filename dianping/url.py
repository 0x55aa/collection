#-*- coding:utf-8 -*-
import cookielib, urllib2
import HTMLParser



class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        #标记在a标签里
        self.aaa=False
        #标记在span里
        self.bbb = False
        self.ccc = False
        #标记标签为ul column
        self.ttt=False
        #self.text=""
        #self.text2=""
        #标题
        self.sampleList=[]
        #个数
        self.numList = []
        #url
        self.URLList=[]
        self.aa=0
     
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            for(varviable,value) in attrs:
                if varviable=="class" and (value=="root-name"):
                    self.aaa=True
                    #self.text2=value
                    #print self.text2
            for(varviable,value) in attrs:
                if varviable=="href" and (self.aaa==True):
                    self.URLList.append(value)
                    #print value
        if tag == 'span' and self.aaa==True:
                self.bbb=True


    def handle_data(self,data):
        if self.bbb == True :
            self.sampleList.append(data.decode('utf-8'))
            #print data.decode('utf-8')
            self.bbb = False
            """
            if len(self.sampleList)!=len(self.URLList):
                self.sampleList.append('a')
            """
            
    def handle_endtag(self,tag):
        """
        if tag == 'span':
            self.bbb = False
        """
        if tag == 'a':
            self.aaa=False

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
            my = MyParser()
            #html1 = my.unescape(html1)
            """
            f = file('a.html','r')
            html = f.read()
            f.close()
            """
            my.feed(html)
            if my.sampleList==[] or my.URLList==[]:
                #print 00
                return False
            else:
                #print my.sampleList
                #print my.numList
                #print my.URLList
                #含有运动健身的城市
                """
                if len(my.sampleList)!=len(my.URLList):
                    for i in range(len(my.URLList)-len(my.sampleList)):
                        del my.URLList[i]
                """
                        
                if "运动健身".decode("utf-8") in my.sampleList:
                    mun = my.sampleList.index("运动健身".decode("utf-8"))
                    #print len(my.sampleList),len(my.URLList)
                    return  my.URLList[mun]
                else:
                    return False
                
                


                
                print len(my.sampleList),len(my.URLList),
                return my.sampleList,my.URLList

        except urllib2.URLError:
            print('connection error')
    def run(self):
        self.get_subject_list(self.tieba_name)


if __name__ == '__main__':
    
    f = file('area0.txt','r')
    areaList = eval(f.readline()[:-1])
    surlList = eval(f.readline())
    f.close()
    #print len(areaList),len(surlList)
    lasturl = []
    lastname = []
    file2 = file("area2.txt",'w+')
    print len(surlList)
    for i in range(280):
        url = 'http://www.dianping.com' + surlList[2000+i]
        t = T_list(url)
        b = t.get_subject_list()
        if b != False:
            #lasturl.append(b)
            #lastname.append(areaList[i])
            #print b,areaList[i]
            file2.write(b)
            file2.write('\n')
            print i
    
    #file2.write(str(lastname))
    #file2.write('\n')
    #file2.write(str(lasturl))
    file2.close()
    print len(lasturl),len(lastname)
    """
    url = 'http://www.dianping.com/chengdu'
    t = T_list(url)
    print t.get_subject_list()
    """

