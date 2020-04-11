# -*- coding: utf-8 -*-
import scrapy


class PeliculasSpider(scrapy.Spider):
    name = 'peliculas'
    allowed_domains = ['imdb.com']
    api_url = 'https://www.filmin.es/catalogo?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
    	self.log('I just visited' +  response.url)

    	titulos = response.css('td.titleColumn')
    	rankings = response.css('td.ratingColumn.imdbRating')

    	for titulo, ranking in zip(titulos, rankings):
    		item = {
    			'titulo': titulo.css('a::text').extract_first(),
    			'ranking': ranking.css('strong::text').extract_first(),
    		}
    		yield item



