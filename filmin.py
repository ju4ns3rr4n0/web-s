import scrapy
#author ju4ns3rr4n0



class FilminSpider(scrapy.Spider):
	name = 'filmin'
	allowed_domains = ['filmin.es']
	api_url = 'https://www.filmin.es/catalogo?page={}'
	page = 1
	start_urls = [api_url.format(page)]

	def parse(self, response):
		urls = response.css('li.col-md-6.col-lg-4.col-xl-3 > div > figure > a::attr(href)').extract()
		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_details)

		if self.page<1:
			self.page += 1
			yield scrapy.Request(url=self.api_url.format(self.page), callback=self.parse)



	def parse_details(self, response):
		yield {
			'titulo': response.css('h1.font-weight-bolder.mb-1::text').extract_first(),
			'rankin': response.css('span.rank::text').extract_first(),
			'genero': response.xpath("//div[@class='info-item'][4]/p/a/text()").extract(),
			'Año': response.xpath("//div[@class='info-item'][3]/p/text()").extract_first(),
			'temas': response.css('a.label-regular>span::text').extract()
		}

