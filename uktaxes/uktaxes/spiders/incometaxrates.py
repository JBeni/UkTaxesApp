import scrapy


class IncometaxratesSpider(scrapy.Spider):
    name = "incometaxrates"
    allowed_domains = ["www.gov.uk"]
    start_urls = ["http://www.gov.uk/"]

    def parse(self, response):
        pass
