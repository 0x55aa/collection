#-*- coding:utf-8 -*-
import cookielib, urllib2
from BeautifulSoup import BeautifulSoup

class T_list:
    
    def __init__(self,url):
        self.t_url = url
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
    def get_subject_list(self):
        try:
            html = urllib2.urlopen(self.t_url).read()
            """
            f = file('a.html','r')
            html = f.read()
            f.close()
            """
            soup = BeautifulSoup(html)
            #print soup.title
            #图片
            print soup.findAll('img', id="prodImage")[0]['src']
            #商品描述
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

        except urllib2.URLError:
            print('connection error')


if __name__ == '__main__':
    url = "http://www.amazon.cn/Actifit-berriology%E7%B3%BB%E5%88%97-%E6%B3%95%E5%9B%BD%E7%BA%A2%E9%85%92%E5%A4%9A%E9%85%9A%E8%83%B6%E5%9B%8A60%E7%B2%92/dp/B00798KTG6"
    t = T_list(url)
    
    t.get_subject_list()

