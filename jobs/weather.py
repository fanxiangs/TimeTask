# -*- coding: UTF-8 -*-
"""
@time:2020/04/06
"""
import requests
from lxml import etree
from TimeTask.send_email import send_eamils


def get_data():
    url = r'http://www.weather.com.cn/weather/101020100.shtml'
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-type": "text/html;charset=UTF-8",
        "Host": "www.weather.com.cn",
    }

    r = session.get(url=url, headers=headers)
    r.encoding = 'utf-8'
    html = etree.HTML(r.text)
    r = html.xpath('//div[@id="7d"]/ul/li[1]/h1')[0]
    sky = html.xpath('//div[@id="7d"]/ul/li[1]/p[1]')[0]
    high = html.xpath('//div[@id="7d"]/ul/li[1]/p[2]/span')[0]
    low = html.xpath('//div[@id="7d"]/ul/li[1]/p[2]/i')[0]
    feng = html.xpath('//div[@id="7d"]/ul/li[1]/p[3]/i')[0]
    # 今天是6日（今天）,天气多云,风级<3级,最高温度至最低温度为16-10℃
    content = '今天是{},天气{},风级{},最高温度至最低温度为{}-{}'.format(r.text, sky.text, feng.text, high.text, low.text, )
    print(content)
    send_eamils(content)


if __name__ == '__main__':
    url = r'http://www.weather.com.cn/weather/101020100.shtml'
    # url = r'http://www.baidu.com/'
    get_data()
