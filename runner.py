import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apartamentos.spiders.metroCuadrado import MetrocuadradoSpider

process = CrawlerProcess(settings =get_project_settings())
process.crawl(MetrocuadradoSpider)
process.start()