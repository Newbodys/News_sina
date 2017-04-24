import scrapy 
import codecs
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.news

class News_sina(scrapy.Spiderhttps):
	name = "News_sina"
	start_urls = []
	url_base = "http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=80&asc=&page="

	for i in xrange(1,10):
		urls = url_base + str(i)
		start_urls.append(urls)
	
	def parse(self,response):
		channel = response.xpath('//span[@class="c_ch1"]/a/text()').extract()
		title = response.xpath('//span[@class="c_tit"]/a/text()').extract()
		time = response.xpath('//span[@class="c_time"]/text()').extract()
		news_content_link = response.xpath('//span[@class="c_tit"]/a/@href').extract()
