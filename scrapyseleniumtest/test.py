#!/usr/bin/env python
# -*-coding:utf-8 -*-\
import requests
from lxml import etree
from requests import Request


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger

# logger = getLogger(__name__)
# browser = webdriver.PhantomJS(service_args=['--load-images=false', '--disk-cache=true'])
# browser.set_window_size(1400, 700)
# browser.set_page_load_timeout(10)
# wait = WebDriverWait(browser, 10)
#
# base_url = 'https://s.taobao.com/search?q=ipad'
#
# browser.get(base_url)
#
# response = browser.page_source

#
# input = wait.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
# )

html_source = '''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><span class='oo'><img src='image1_thumb.jpg' />in span <dd>in the dd</dd><mm>in the mm</mm></span></a>
   <a href='image1.html'>Name: My image 1 <br /><span class='oo'><img src='image1_thumb.jpg' />in span <dd>in the dd</dd><mm>in the mm</mm></span></a>
   <a href='image1.html'>Name: My image 1 <br /><span class='oo'><img src='image1_thumb.jpg' />in span <dd>in the dd</dd><mm>in the mm</mm></span></a>
   <a href='image1.html'>Name: My image 1 <br /><span class='oo'><img src='image1_thumb.jpg' />in span <dd>in the dd</dd><mm>in the mm</mm></span></a>
   <a href='image1.html'>Name: My image 1 <br /><span class='oo'><img src='image1_thumb.jpg' />in span <dd>in the dd</dd><mm>in the mm</mm></span></a>
  </div>
 </body>
</html>
 '''
html = etree.HTML(html_source)
ret = html.xpath('//div[@id="images"]//a')
for i in ret:
    print(i.xpath('.//span[contains(@class, "oo")]//text()'))

# ret = html.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]')
# ret = html.xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"][2]/@id')
# for product in ret:
    # print(type(product))
    # print(product.xpath('.//div[contains(@class, "price")]//text()'))
    # a = product.xpath('.//div[contains(@class, "price")]//text()')
    # a = ''.join(product.xpath('.//div[contains(@class, "price")]//text()').extract()).strip()
    # a = ''.join(product.xpath('.//div[contains(@class, "price")]//text()').extract()).strip()
    # print('----------------------')












