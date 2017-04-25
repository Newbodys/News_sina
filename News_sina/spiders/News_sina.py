import scrapy 
import codecs
from pymongo import MongoClient
from scrapy.selector import Selector

client = MongoClient('localhost',27017)
db = client.news


class News_sina(scrapy.Spider):

class News_sina(scrapy.Spiderhttps):
	name = "News_sina"
	start_urls = []
	url_base = "http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=80&asc=&page="

	for i in xrange(1,10):
		urls = url_base + str(i)
		start_urls.append(urls)
	
	def parse(self,response):
		body_li = response.xpath('//li').extract()
		for i in body_li:
			#sel = Selector(text=i)
			title = Selector(text=i).xpath('//span[@class="c_tit"]/a/text()').extract()
			time = Selector(text=i).xpath('//span[@class="c_time"]/text()').extract()
			news_content_link = Selector(text=i).xpath('//span[@class="c_tit"]/a/@href').extract()
			#print news_content_link[0]
			document = ({
				#'channel':channel[i],
				'title':title,
				'time':time,
				'news_content_link':news_content_link,
				'news_content':"",
				})
			db.news_list.insert(document)

			yield scrapy.Request(url=news_content_link[0],callback=self.parse_page)

		'''#channel = response.xpath('//span[@class="c_ch1"]/a/text()').extract()
		title = response.xpath('//span[@class="c_tit"]/a/text()').extract()
		c_time = response.xpath('//span[@class="c_time"]/text()').extract()
		news_content_links = response.xpath('//span[@class="c_tit"]/a/@href').extract()
		for i in xrange(len(news_content_links)):
			document = ({
				#'channel':channel[i],
				'title':title[i],
				'time':c_time[i],
				'news_content_link':news_content_links[i],
				'news_content':"",
				})
			db.news_list.insert(document)

		for url_content in news_content_links:
			yield scrapy.Request(url=url_content,callback=self.parse_page)'''

	def parse_page(self,response):
		news_content = response.xpath('//div[@class="article-a__content"]/p').extract()
		db.news_list.update({"news_content_link":response.url},{'$set':{"news_content":news_content}})
