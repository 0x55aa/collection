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
        #self.ccc = False
        #标记标签为ul column
        self.ttt=False
        #self.text=""
        #self.text2=""
        #标题
        self.sampleList=[]
        #下一页
        self.nextList = []
        #url
        self.URLList=[]
     
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'div':
            # 判断标签<a>的属性
            for(varviable,value) in attrs:
                if varviable=="class" and (value=="productTitle"):
                    self.ttt=True

        if tag == 'span':
            # 判断标签<a>的属性
            for(varviable,value) in attrs:
                if varviable=="class" and (value=="pagnNext"):
                    self.bbb = True
                    
        if tag == 'a' and self.ttt==True:
            for(varviable,value) in attrs:
                if varviable=="href":
                    self.aaa=True
                    #self.text2=value
                    #print self.text2
                    self.URLList.append(value)
                    #print value
        if tag == 'a' and self.bbb==True:
            for(varviable,value) in attrs:
                if varviable=="href":
                    self.bbb=False
                    #self.text2=value
                    #print self.text2
                    self.nextList.append(value)
                    #print value

    def handle_data(self,data):
        if self.aaa == True :
            #self.text = data
            #print self.text.decode('gbk')
            #print repr(data.decode('utf-8'))
            self.sampleList.append(data.decode('utf-8'))
            #print data.decode('utf-8')
            

            
    def handle_endtag(self,tag):
        if tag == 'a':
            self.aaa=False
        if tag == 'div':
            self.ttt=False

class T_list:
    
    def __init__(self,url):
        self.t_url = url
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
    def get_subject_list(self):
        try:
            html = urllib2.urlopen(self.t_url).read()
            #print html
            """
            f=file('b.html','w')
            f.write(html)
            f.close()
            """
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
                return my.sampleList,my.URLList,my.nextList

        except urllib2.URLError:
            print('connection error')
            
    def run(self):
        
        for u in c:
            tt = T_list(u)
            d,e,f = tt.get_subject_list()
            

if __name__ == '__main__':
    url = 'http://www.amazon.cn/gp/search/ref=sr_in_-2_p_4_83?rh=n%3A852803051%2Cn%3A!852804051%2Cn%3A836317051%2Cp_4%3A%E7%BE%8E%E5%81%A5%E5%A4%A9%E8%87%A3&bbn=836317051&ie=UTF8&qid=1342535413&rnid=863865051'
    
    t = T_list(url)
    aa,bb,c = t.get_subject_list()
    print c
    while c:
        tt = T_list(c[0])
        a,b,c = tt.get_subject_list()
            
        aa += a
        bb += b
        

    print len(aa),len(bb)


