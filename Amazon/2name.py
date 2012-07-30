#-*- coding:utf-8 -*-
import cookielib, urllib2
import HTMLParser



class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        #标记在a标签里
        self.aaa=False
        #标记在span里
        #self.bbb = False
        #self.ccc = False
        #标记标签为ul column
        self.ttt=False
        #self.text=""
        #self.text2=""
        #标题
        self.sampleList=[]
        #个数
        #self.numList = []
        #url
        self.URLList=[]
     
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'div':
            # 判断标签<a>的属性
            print 9
            for(varviable,value) in attrs:
                if varviable=="class" and (value=="productTitle"):
                    self.ttt=True
                    
        if tag == 'a' and self.ttt==True:
            for(varviable,value) in attrs:
                if varviable=="href":
                    self.aaa=True
                    #self.text2=value
                    #print self.text2
                    self.URLList.append(value)
                    print value

    def handle_data(self,data):
        if self.aaa == True :
            #self.text = data
            #print self.text.decode('gbk')
            #print repr(data.decode('utf-8'))
            self.sampleList.append(data.decode('utf-8'))
            print data.decode('utf-8')
            

            
    def handle_endtag(self,tag):
        if tag == 'a':
            self.aaa=False
        if tag == 'div':
            self.ttt=False

class T_list:
    t_url = 'http://www.amazon.cn/999%E4%BC%98%E8%8A%9D%E4%B8%8A%E5%93%81-%E5%B7%A6%E6%97%8B%E8%82%89%E7%A2%B1%E8%8C%B6%E5%A4%9A%E9%85%9A%E8%83%B6%E5%9B%8A-0-35g-%E7%B2%92%C3%9730%E7%B2%92-%E8%A2%8B%C3%972%E8%A2%8B/dp/B007B8J7HG'
    
    def __init__(self):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
    def get_subject_list(self):
        try:
            html = urllib2.urlopen(self.t_url).read()
            #print html
            
            f=file('d.html','w')
            f.write(html)
            f.close()
            
            my = MyParser()
            my.feed(html)
            if my.sampleList==[] or my.URLList==[]:
                print '00'
                return False
            else:
                #print my.sampleList
                #print my.numList
                #print my.URLList
                print len(my.sampleList),len(my.URLList)#,len(my.numList),
                return my.sampleList,my.URLList

        except urllib2.URLError:
            print('connection error')
    def run(self):
        self.get_subject_list(self.tieba_name)


if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding( "utf-8" ) 
    t = T_list()
    
    t.get_subject_list()

