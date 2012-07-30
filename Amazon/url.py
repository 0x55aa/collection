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
        if tag == 'ul':
            # 判断标签<a>的属性
            for(varviable,value) in attrs:
                if varviable=="class" and (value=="column"):
                    self.ttt=True
        if tag == 'a' and self.ttt==True:
            for(varviable,value) in attrs:
                if varviable=="href":
                    self.aaa=True
                    #self.text2=value
                    #print self.text2
                    self.URLList.append(value)
                    #print self.sampleList
        if tag == 'span' and self.ttt==True:
            for(varviable,value) in attrs:
                if varviable=="class" and (value=="refinementLink"):
                    self.bbb=True
        if tag == 'span' and self.ttt==True:
            for(varviable,value) in attrs:
                if varviable=="class" and (value=="narrowValue"):
                    self.ccc=True

    def handle_data(self,data):
        if self.bbb == True :
            #self.text = data
            #print self.text.decode('gbk')
            #print repr(data.decode('utf-8'))
            self.sampleList.append(data.decode('utf-8'))
            #print data.decode('utf-8')
        if self.ccc == True :
            self.numList.append(data.decode('utf-8'))
            self.aa = self.aa+int(repr(data)[2:-2])
            print data.decode('utf-8')
            print self.aa
            
    def handle_endtag(self,tag):
        if tag == 'span':
            self.bbb = False
            self.ccc = False
        if tag == 'a':
            self.aaa=False
        if tag == 'ul':
            self.ttt=False

class T_list:
    t_url = 'http://www.amazon.cn/gp/search/other?rh=n%3A852803051%2Cn%3A!852804051%2Cn%3A836317051&bbn=836317051&pickerToList=brandtextbin&ie=UTF8&qid=1341991494&rd=1'
    
    def __init__(self):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
    def get_subject_list(self):
        try:
            html = urllib2.urlopen(self.t_url).read()
            my = MyParser()
            #html1 = my.unescape(html1)
            f = file('a.html','r')
            html = f.read()
            f.close()
            my.feed(html)
            if my.sampleList==[] or my.URLList==[]:
                #print 00
                return False
            else:
                #print my.sampleList
                #print my.numList
                #print my.URLList
                print str(my.aa)
                print len(my.sampleList),len(my.URLList),len(my.numList),
                return my.sampleList,my.URLList

        except urllib2.URLError:
            print('connection error')
    def run(self):
        self.get_subject_list(self.tieba_name)


if __name__ == '__main__':
    t = T_list()
    
    t.get_subject_list()

